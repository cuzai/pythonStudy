import pytube
import os
import subprocess
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

yTube = pytube.YouTube("https://www.youtube.com/watch?v=HosW0gulISQ")
video = yTube.streams.all()

#for i in range(len(video)) :
#    print(i, video[i])

downDir = 'C:/Users/cuzai/Desktop/Web_Crawling/youtube'

oriFileName = video[0].default_filename
newFileName = "new.mp3"

subprocess.call(['ffmpeg', '-i',
    os.path.join(downDir, oriFileName),
    os.path.join(downDir, newFileName)
])

video[0].download(downDir)


print("done")
