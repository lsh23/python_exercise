from bs4 import BeautifulSoup
import sys
import io
from urllib.request import urlopen

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

for i in range(1,8):
    url = urlopen("https://music.bugs.co.kr/chart/track/day/total?chartdate=2019010"+str(i))
    soup = BeautifulSoup(url,"lxml")
    a = (soup.find_all(name="time"))
    b = a[0].text
    b



    print("--------------------------------------------------")
    cnt_artist = 0
    cnt_title = 0
    for link1,link2 in zip(soup.find_all(name="p",attrs={"class":"artist"}),soup.find_all(name="p",attrs={"class":"title"})):
        cnt_artist += 1
        print(str(cnt_artist) + "위")
        print("아티스트 : "+link1.find('a').text)
        print("제목 : "+link2.find('a').text)
        if(cnt_artist == 10):
            break
