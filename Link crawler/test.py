import requests






r = requests.head("http://www.ahzixun.cn", allow_redirects = True)
__content = r.headers
cc = __content.get('Content-Type')

print(cc)