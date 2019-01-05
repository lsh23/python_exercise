import pytube
import os
import subprocess
# subprocess가 cmd 프로세스환경에서 작업할 수 있게끔 해줌
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#다운 받을 동영상 URL 지정

input_url = input("다운 받을 youtube 주소를 입력해주세요")
yt = pytube.YouTube(input_url)
videos = yt.streams.all()

for i in range(len(videos)) :
        print(i, ' , ', videos[i])


cNum = int(input("다운 받을 화질은? (0~21 입력)"))

down_dir = "C:\\youtube"

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
])

print("동영상 다운 및 mp3 변환 완료")
