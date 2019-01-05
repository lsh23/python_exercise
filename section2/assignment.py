import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1215/1215078/10317821c7fc63a8d1e0_20181130185818999_1.png"
clipUrl =  "https://tvetamovie.pstatic.net/libs/1220/1220927/9c856be88b643113ef82_20190103133044925.mp4-pBASE-v0-f71415-20190103133123434.mp4"

savePath1 = "C:\\assignment.jpg"
savePath2 = "C:\\assignnent_.mp4"

req.urlretrieve(imgUrl,savePath1)
req.urlretrieve(clipUrl,savePath2)

print("다운로드 완료")
