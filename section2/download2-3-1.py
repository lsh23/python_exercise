import sys
import io
import urllib.request as req
from urllib.parse import urlparse
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://computer.cnu.ac.kr"

mem = req.urlopen(url)

# print(type(mem))
# print(type({}))
# print(type([]))
# print(type(()))

# print("geturl",mem.geturl())
# print("status",mem.status) #200 , 404 , 403, 500
#                            #정상 , 오류 , 보호(접근불가) , 서버오류
# print("headers",mem.getheaders())
# print("info",mem.info())
# print("code",mem.getcode())
# print("read",mem.read().decode("utf-8"))
print(urlparse("url"))
