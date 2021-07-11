print(
    '─██████████████─────────██████─\n'
    '─██░░░░░░░░░░██─────────██░░██─\n'
    '─██░░██████████─────────██░░██─\n'
    '─██░░██─────────────────██░░██─\n'
    '─██░░██████████─────────██░░██─\n'
    '─██░░░░░░░░░░██─────────██░░██─\n'
    '─██░░██████████─██████──██░░██─\n'
    '─██░░██─────────██░░██──██░░██─\n'
    '─██░░██████████─██░░██████░░██─\n'
    '─██░░░░░░░░░░██─██░░░░░░░░░░██─\n'
    '─██████████████─██████████████-\n'
)
print('Welcome to YouTube Downloader and Converter Beta')
print('Loading...')

from install_packages import install_packages
install_packages(['pytube', 'moviepy'])

import pytube
import youtube_downloader
from file_converter import convert_to_mp3

print('''
What do you want?

(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3

Downloading copyrighted YouTube videos is illegal!
I am not responsible for your downloads! Go at your own risk!

''')

choice = input('Choice: ')

if choice == '1' or choice == '2':
    quality = input('Please choose a quality (low, medium, high, very high):')
    if choice == '2':
        link = input('Enter the link to the playlist: ')
        print('Downloading playlist...')
        youtube_downloader.download_playlist(link, quality)
        print('Download finished!')
    if choice == '1':
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == '3':
    links = youtube_downloader.input_links()
    for link in links:
        print('Downloading...')
        filename = youtube_downloader.download_video(link, 'low')
        print('Converting...')
        convert_to_mp3(filename)
else:
    print('Invalid input! Terminating...')
