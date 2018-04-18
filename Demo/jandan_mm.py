# _*_ encoding: utf-8 _*_

from urllib import request, error, parse
from bs4 import BeautifulSoup


class Spider:
    """ 爬取妹子图 """

    def __init__(self):
        self.base_url = "http://jandan.net/ooxx"

    def get_page_content(self, page_num):
        """ 获得某一页的web内容 """

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/27.0.1453.94 Safari/537.36',
            'Connection': 'keep-alive'
        }

        page_url = self.base_url + "/" + str(page_num)
        req = request.Request(page_url, headers=header)
        res = request.urlopen(req).read().decode('utf-8')
        print(res)

        return res

spider = Spider()
spider.get_page_content(1)