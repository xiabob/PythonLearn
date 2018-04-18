from urllib import request, parse
import xiciProxys
import QSBK

# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read())

# values = {}
# values['action'] = "login"
# values['email'] = "xiabob@yeah.net"
# values['password'] = "F26pfD13Gol5"
# values['rememberme'] = 'on'

# or using

values = {
    'action': 'login',
    'email': 'xiabob@yeah.net',
    'password': 'F26pfD13Gol5',
    'rememberme': 'on'
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)' 
                    ' Chrome/27.0.1453.94 Safari/537.36',
    'Connection': 'keep-alive'
}

data = parse.urlencode(values).encode('utf-8')

req = request.Request("http://lkong.cn/index.php?mod=login", headers=header, data=data)
resp = request.urlopen(req).read()

print(resp.decode('utf-8'))


QSBK.start()
