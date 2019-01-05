import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20090918_6/sunmoon8874_1253260279597y5kIx_jpg/9_sunmoon8874.jpg"
#savePath = "test1.jpg"
# 이렇게 되면 현재 경로에 저장 / 절대 주소를 적어서 원하는 곳을 적어주는 것이 좋음
htmlURL = "http://google.com"

savePath = "C:\\test1.jpg"
savePath2 = "C:\\index.html"
# C:\\로하면 진짜 C드라이브 그자체에 저장되고
# c:/로하면 USER로 자동으로 넘어가서 c:/user에 저장됨

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath, 'wb') # w : wirte , r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)


# with 는 반납을 자동으로 해줌 with문을 벗어나면 자동으로 close() 해줌


print("다운로드 완료")
