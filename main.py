from pytube import YouTube
from sys import argv    

link = argv[1]
yt = YouTube(link)

#print yt title
print(yt.title)
#print number of views
print(yt.views)

#download
yd = yt.streams.get_highest_resolution()
yd.download#(path to download video)