# -*- coding:utf-8 -*-

import argparse
import hashlib
import hmac
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import pprint
import os
import sys
import requests  # https://zhuanlan.zhihu.com/p/25589547

# https://eli.thegreenplace.net/2014/07/09/payload-server-in-python-3-for-github-webhooks


class GithubHookHandler(BaseHTTPRequestHandler):
    """Base class for webhook handlers.

    Subclass it and implement 'handle_payload'.
    """
    def do_POST(self):

        data_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(data_length)
        payload = json.loads(post_data.decode('utf-8'))
        self.handle_payload(payload)
        self.send_response(200, 'ok')


class MyHandler(GithubHookHandler):

    def handle_payload(self, json_payload):
        """Simple handler that pretty-prints the payload."""
        pprint.pprint(json_payload)

        # origin_data = json.load(json_payload)
        data = {}
        if json_payload['eventType'] == 'bugly_crash_trend':
            event_content = json_payload['eventContent']
            crash_contents = event_content['datas']

            post_contet = '应用名：' + event_content['appName'] + '  '
            post_contet += '平台：' + str(event_content['platformId']) + '  '
            post_contet += '日期：' + event_content['date'] + '\n'
            post_contet += 'bugly app url：' + event_content['appUrl'] + '\n'
            post_contet += '\n=========Top ' + str(len(crash_contents)) + ' Crash=========\n'
            for crash in crash_contents:
                post_contet += '联网用户数：' + str(crash['accessUser']) + '\n'
                post_contet += 'crash次数：' + str(crash['crashCount']) + '\n'
                post_contet += 'crash影响用户数：' + str(crash['crashUser']) + '\n'
                post_contet += 'app版本号：' + crash['version'] + '\n'
                post_contet += 'url：' + crash['url'] + '\n'
                if crash_contents[len(crash_contents)-1] != crash:
                    post_contet += '--------------分割线-------------\n\n'

            data['title'] = 'Bugly Crash Report'
            data['text'] = post_contet
            self.send_to_feishu_webhook(data)

        elif json_payload['eventType'] == 'bugly_tag':
            data['title'] = 'Bugly Tag'
            data['text'] = '测试'
            self.send_to_feishu_webhook(data)

    def send_to_feishu_webhook(self, data):
        # https://open-lf.feishu.cn/open-apis/bot/hook/a8eb160c31cd4360b1b1550f50e521c4

        url = 'https://open-lf.feishu.cn/open-apis/bot/hook/a8eb160c31cd4360b1b1550f50e521c4'
        # data = {
        #     'title': "123",
        #     'text': "456"
        # }
        requests.post(url, json=data)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='common hook handler')
    argparser.add_argument('port', type=int, help='TCP port to listen on')
    args = argparser.parse_args()

    server = HTTPServer(('', args.port), MyHandler)
    server.serve_forever()