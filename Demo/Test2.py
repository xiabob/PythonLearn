# _*_ encoding utf-8 _*_

from urllib import request, parse, error
import xiciProxys
from TieBa import BDTB


header = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)' 
                  'Chrome/27.0.1453.94 Safari/537.36'),
    ('Connection', 'keep-alive')
]

values = {
    'action': 'login',
    'email': 'xiabob@yeah.net',
    'password': 'F26pfD13Gol5',
    'rememberme': 'on'
}

data = parse.urlencode(values).encode('utf-8')

proxies = xiciProxys.get_proxies()

# 创建ProxyHandler
proxy_support = request.ProxyHandler(proxies[5])

# Create Opener
opener = request.build_opener(proxy_support)

# add header
opener.addheaders = header

# install opener 之后的请求都会走代理
request.install_opener(opener)

try:

    # 使用自己安装好的Opener
    response = request.urlopen('http://lkong.cn/index.php?mod=login', data)

    # response = request.urlopen("http://www.whatismyip.com.tw/")
    html = response.read().decode('utf-8')
    print(html)

except error.HTTPError as e:
    print(e)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)


