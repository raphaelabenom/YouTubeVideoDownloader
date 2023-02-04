#Youtube video download
from pytube import YouTube
#Entry your video link
video = YouTube("Video link")
streams = video.streams.filter(progressive=True).order_by("resolution").last()
streams.download()
print("Video Downloaded")
