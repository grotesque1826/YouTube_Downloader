from pytube import *

url = "https://www.youtube.com/watch?v=LOZNKZfiFUw"
path = "C:\\Users\\Sam\\Desktop"
ob = YouTube(url)

#strm = ob.streams.first()
strms = ob.streams.all()
for s in strms:
   print(s)
#print(strm.title)
#print(strm.filesize)
#strm.download(path)
#print("done...")