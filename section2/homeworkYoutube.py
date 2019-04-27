import pytube
import os
import subprocess

count = 0
myUrls = []
myVideos = []
inputNames = []
savedFiles = []
saveDirs = []
downDir = 'C:/Users/cuzai/Desktop/Web_Crawling'

url = input("put the url : ")


myUrls.append(url)

while True :
    myInput = input("one more? : ")
    if myInput == 'y' :
        count += 1
        moreUrl = input("put the url : ")
        myUrls.append(moreUrl)
        continue
    elif myInput == 'n':
        break
    else :
        print("invaid answer")

isConvert = input("do you want to convert to mp3? : ")

for j in range(len(myUrls)) :
    myVideos.append(pytube.YouTube(myUrls[j]).streams.first())
    myVideos[j].download(downDir)

if isConvert == 'y' :
    for i in range(len(myVideos)) :
        inputNames.append(input("put video{} name : ".format(i)))
        savedFiles.append(os.path.join(downDir, myVideos[i].default_filename))
        saveDirs.append(os.path.join(downDir, inputNames[i]))
        print(savedFiles[i])
        print(saveDirs[i])

    for i in range(len(myVideos)) :
        subprocess.call(['ffmpeg', '-i',
            savedFiles[i], saveDirs[i]
        ])

print("done")
