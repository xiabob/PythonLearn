
# _*_ encoding utf-8 _*_

from bs4 import BeautifulSoup
from urllib import request, parse, error
import time
import socket
import random


def get_web_content(url):
    """ Gey the web site content"""

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'}
    req = request.Request(url, headers=header)              # request

    while True:
        try:
            response = request.urlopen(req).read()          # web site content
            break
        except error.HTTPError as e:                        # output log to debug easily
            print(1 + e)
            time.sleep(random.choice(range(5, 20)))
        except error.URLError as e:
            print(2 + e)
            time.sleep(random.choice(range(10, 30)))
        except socket.timeout as e:
            print(3 + e)
            time.sleep(random.choice(range(15, 20)))
        except Exception as e:
            print(4 + e)
            time.sleep(random.choice(range(10, 20)))

    return response


def extract_ip_address(content):
    """ Extract web IP address and port """

    proxies = []                                     # proxy list
    soup = BeautifulSoup(content, "html.parser")    # soup object
    trs = soup.find_all('tr')                       # extract tr tag
    for tds in trs[1:]:
        td = tds.find_all('td')

        # get proxy type: http or https
        proxy_type = str(td[5].contents[0]).lower()

        # get url host: port
        proxy_url = str(td[1].contents[0]) + ":" + str(td[2].contents[0])

        proxies.append({proxy_type: proxy_url})

    return proxies


def get_proxies():
    """ main function """

    url = 'http://www.xicidaili.com/nn/1'
    content = get_web_content(url)
    proxies = extract_ip_address(content)

    # need filter process

    for e in proxies:
        print(e)

    return proxies
