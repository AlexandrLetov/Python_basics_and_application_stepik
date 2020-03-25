import requests
import re

A = input()
B = input()


def request(_url):
    res = requests.get(_url)
    return(str(res.content))


def reg(url_list):
    urlre = re.compile('<a[^>]+href="([^"]+)"[^>]*>', re.IGNORECASE)
    urls_list = urlre.findall(url_list)
    for item in urls_list:
        item = 'https://' + item
    return(urls_list)


list_A = reg(request(A))
list_B = []


for item in list_A:
    urls = request(item)
    for obj in reg(urls):
        list_B.append(obj)

flag = 'No'

if B in list_B:
    flag = 'Yes'
print(flag)
