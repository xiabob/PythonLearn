# _*_ encoding utf-8 _*_

from urllib import request, error, parse
from bs4 import BeautifulSoup


def get_web_content(page):
    """ 获得某一页web文本原始内容 """

    url = "http://www.qiushibaike.com/hot/page/" + str(page)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
    }

    req = request.Request(url, headers=header)

    try:
        response = request.urlopen(req)

        return response.read().decode('utf-8')

    except error.URLError as e:
        print(e)

    except error.HTTPError as e:
        print(e)

    except Exception as e:
        print(e)


def parse_web_content(content):
    """ 解析web原始内容，得到笑话集合 """

    contents = []

    soup = BeautifulSoup(content, "html.parser")
    content_tags = soup.find_all("div", {"class": "content"})
    for contentTag in content_tags:
        span_tag = contentTag.find_all("span")[0]
        content_string = str(span_tag.contents[0])
        contents.append(content_string)

    return contents


def start():
    content = get_web_content(1)
    contents = parse_web_content(content)
    for detail in contents:
        print(detail)

