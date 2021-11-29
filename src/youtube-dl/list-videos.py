from __future__ import unicode_literals
from youtube_dl import YoutubeDL
from csv import DictWriter
from sys import argv

options = {}
channel_url = argv[1]
fieldnames = ['id', 'title', 'duration', 'upload_date']

with YoutubeDL(options) as ydl:
      channel = ydl.extract_info(channel_url, download=False)
      videos = channel['entries']
      videos = ({key: video[key] for key in fieldnames} for video in videos)
      with open(f'{channel["id"]}.channel.youtube.csv', 'w') as csv_file:
          writer = DictWriter(csv_file, fieldnames=fieldnames)
          writer.writeheader()
          writer.writerows(videos)
