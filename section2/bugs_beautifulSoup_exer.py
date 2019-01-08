from bs4 import BeautifulSoup
import sys
import io
from urllib.request import urlopen

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = urlopen("https://music.bugs.co.kr/chart/track/day/total?chartdate=20190107")
soup = BeautifulSoup(url,"lxml")
cnt_artist = 0
cnt_title = 0

for link1,link2 in zip(soup.find_all(name="p",attrs={"class":"artist"}),soup.find_all(name="p",attrs={"class":"title"})):
    cnt_artist += 1
    print(str(cnt_artist) + "위")
    print("아티스트 : "+link1.find('a').text)
    print("제목 : "+link2.find('a').text)
