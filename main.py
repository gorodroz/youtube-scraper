from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Paste Link:")

video = YouTube(
    url=url,
    on_progress_callback=on_progress,
    use_oauth=False,
    allow_oauth_cache=False
)

print('Title:', video.title)
print("Which format you want to download? Audio or Video")
ytaudvid = input("")
if ytaudvid == "Audio":
    audio = video.streams.filter(only_audio=True)
    print(video.streams.filter(only_audio=True))
    stream = video.streams.get_by_itag(input("Write itag for download:"))
if ytaudvid == "Video":
    ovideo = video.streams.filter(file_extension='mp4')
    print(video.streams.filter(file_extension='mp4'))
    stream = video.streams.get_by_itag(input("Write itag for download:"))

print("Do you want to change path for download? Write Yes or No.")
pathdownload = input("")
if pathdownload == "Yes":
    stream.download(output_path=input("Enter path:"))
elif pathdownload == "No":
    stream.download(output_path="X:\youtube-scraper\downloads")

print("Successful!")

