import urllib.request
from urllib.error import URLError
from urllib.error import HTTPError

try:
    headers={'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    response=urllib.request.Request("http://python.org/",headers=headers)

    html=urllib.request.urlopen(response)

    result= html.read().decode('utf-8')

except URLError as e:
    if hasattr(e,'reason'):
        print('URLError 错误原因'+str(e.reason))
except HTTPError as e:
    if hasattr(e,'reason'):
        print('HTTPError 错误原因'+str(e.reason))
else:
    print('请求通过')

