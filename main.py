from pytubefix import YouTube
from pytubefix.cli import on_progress

quality_vid = {
    "360p mp4": "18",
    "2160p no audio": "701",
    "1440p no audio": "700",
    "1080p no audio": "137",
    "720p no audio": "136",
    "480p no audio": "135",
    "360p no audio": "134",
    "240p no audio": "133",
    "144p no audio": "160"
}

quality_aud = {
    "160kbps opus": "251",
    "128kbps m4a": "140",
    "50kbps m4a": "249",
    "48kbps m4a": "139"
}

url = input("Paste Youtube Link:")

video = YouTube(
    url=url,
    on_progress_callback=on_progress,
    use_oauth=False,
    allow_oauth_cache=False
)
minsmedia = int(video.length/60)

print('Title:', video.title, minsmedia, "mins")
print("Which format you want to download? \"Audio\" or \"Video\"")
ytaudvid = input("")
if ytaudvid == "Audio":
    audio = video.streams.filter(only_audio=True)
    userqlt = input(f"Choice quality {list(quality_aud.keys())}: ")
    getqlt = quality_aud.get(userqlt)
    if not getqlt:
        print("Error. You enter unavaible quality. Exit")
        exit()
    stream = video.streams.get_by_itag(getqlt)

if ytaudvid == "Video":
    ovideo = video.streams.filter(file_extension='mp4')
    userqlt = input(f"Choice quality {list(quality_vid.keys())}: ")
    getqlt = quality_vid.get(userqlt)
    if not getqlt:
        print("Error. You enter unavaible quality. Exit")
        exit()
    stream = video.streams.get_by_itag(getqlt)

print("Do you want to change path for download? Write \"Yes\" or \"No\".")
pathdownload = input("")
if pathdownload == "Yes":
    stream.download(output_path=input("Enter path:"))
elif pathdownload == "No":
    stream.download(output_path="X:\youtube-scraper\downloads")

print("Successful!")