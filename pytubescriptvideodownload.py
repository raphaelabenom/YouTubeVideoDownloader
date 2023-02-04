#Youtube video download
from pytube import YouTube
#Entry your video link
video = YouTube("https://www.youtube.com/watch?v=_Eb0utIRdkw&list=PL7RwtdVQXQ8qxBH6ugYn50D0M5u--2Xx4")
streams = video.streams.filter(progressive=True).order_by("resolution").last()
streams.download()
print("Video Downloaded")
