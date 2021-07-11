import pytube
from pytube.cli import on_progress
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url, on_progress_callback=on_progress)
    stream = video.streams.get_by_itag(itag)
    print(stream.title)
    stream.download()
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ['low', '360', '360p']:
        itag = 18
    elif resolution in ['medium', '720', '720p', 'hd']:
        itag = 22
    elif resolution in ['high', '1080', '1080p', 'fullhd', 'full_hd', 'full hd']:
        itag = 137
    elif resolution in ['very high', '2160', '2160p', '4K', '4k']:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print('Enter the links of the videos (end by entering "STOP"):')

    links = []
    link = ''

    while link not in ['STOP', 'stop']:
        link = input()
        links.append(link)

    links.pop()

    return links