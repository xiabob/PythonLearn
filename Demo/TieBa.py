# _*_ encoding utf-8 _*_

from bs4 import BeautifulSoup
from urllib import request, error, parse
import re


class Tool:
    """ 工具类 """

    removeImg = re.compile('<img.*?>| {7}|')            # 去除img标签，或者7位长空格
    removeAddr = re.compile('<a.*?>|</a>')              # 删除超链接标签
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')  # 将换行标签换为\n
    replaceTD = re.compile('<td>')                      # 将表格制表<td>替换为\t
    replacePara = re.compile('<p.*?>')                  # 把段落开头换为\n加空两格
    replaceBR = re.compile('<br><br>|<br>')             # 将换行符或双换行符替换位\n
    removeExtraTag = re.compile('<.*?>')                # 删除其余标签

    def replace(self, x):
        x = re.sub(self.removeImg, '', x)
        x = re.sub(self.removeAddr, '', x)
        x = re.sub(self.replaceLine, '\n', x)
        x = re.sub(self.replaceTD, '\t', x)
        x = re.sub(self.replacePara, '\n  ', x)
        x = re.sub(self.replaceBR, '\n', x)
        x = re.sub(self.removeExtraTag, '', x)

        # 去除开头结尾的空白字符
        return x.strip()


class BDTB:
    """ 百度贴吧爬虫类 """

    def __init__(self, base_url, see_lz):
        """ 初始化，传入基地址，是否只看楼主参数 """
        self.base_url = base_url
        self.see_lz = see_lz
        self.tool = Tool()

    def get_page(self, page_num):
        """ 传入页码，获得该页的帖子 """
        try:
            full_url = self.base_url + "?see_lz=" + str(self.see_lz) + "&pn=" + str(page_num)
            req = request.Request(full_url)
            response = request.urlopen(req)
            # print(response.read().decode("utf-8"))

            return response.read().decode('utf-8')
        except error.URLError as e:
            print(e)
        except error.URLError as e:
            print(e)
        except Exception as e:
            print(e)

    def get_title(self):
        """ 获得帖子标题 """
        page = self.get_page(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)

        if result:
            return result.group(1).strip()
        else:
            return None

    def get_page_num(self):
        """ 获取帖子一共有多少页 """

        # 分析页面中"共？页"得到页数
        page = self.get_page(1)
        pattern = re.compile('<li class="l_reply_num".*?</span>.*?<span.*?>(.*?)</span>.*?</li>', re.S)
        result = re.search(pattern, page)
        if result:
            return int(result.group(1).strip())
        else:
            return None

    def get_contents(self, page):
        """ 获得某一页所有楼层的正文内容 """

        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        floor = 1
        for item in items:
            print("\n" + str(floor) + u"楼--------------------------------------------"
                               u"------------------------------------------------"
                               u"----------------------------------------\n")
            print(self.tool.replace(item))
            floor += 1

url = "http://tieba.baidu.com/p/5633146109"
bdtb = BDTB(url, 0)
# bdtb.get_page(1)

# print(bdtb.get_title())
# print(bdtb.get_page_num())
# bdtb.get_contents(bdtb.get_page(1))

num = bdtb.get_page_num()
i = 1
while i <= num:
    bdtb.get_contents(bdtb.get_page(i))
    i += 1


