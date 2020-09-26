# v0.1
#
# To do
# Implememt config.ini containing URL of media categories

# import moviepy
import io
import json
from moviepy.editor import *
#import moviepy.editor as mpy

import requests

def theme_page_download(url, html_output):
  r = requests.get(url)

  with open(html_output, 'wb') as f:
    f.write(r.content)

def theme_page_extract(html_file):
  with open(html_file, 'r') as f:
    j = json.load(f)

    media_liste = []

    for i in range(5):
      title = j['category']['media'][i]['title']
      media_url = j['category']['media'][i]['files'][0]['progressiveDownloadURL']
      media_filename = media_url.split('/')[-1][:-4]

      media_liste.append([title, media_url, media_filename])

    return media_liste

def mp4_download_write_and_convert(mp4_url, mp4_output):
  s = requests.get(mp4_url)

  with open(mp4_output+".mp4", 'wb') as f:
    f.write(s.content)
    video = VideoFileClip(mp4_output+".mp4")
    video.audio.write_audiofile(mp4_output+".mp3")

def mp4_dowload_and_direct_convert(mp4_url, mp4_output):
  t = requests.get(mp4_url)

#  inmemoryfile = io.BytesIO(t.content)

  #video = VideoFileClip(mp4_output+".mp4")
  #video.audio.write_audiofile(mp4_output+".mp3")

  video = mpy.VideoClip(t.content)
  video.audio.write_audiofile(mp4_output+".mp3")

def main():
#  morning_worship_URL = 'https://b.jw-cdn.org/apis/mediator/v1/categories/E/VODPgmEvtMorningWorship'
#  mp4_url="https://download-a.akamaihd.net/files/media_periodical/f7/jwbmw_E_201410_03_r240p.mp4"
#  theme_page_download("filename.html")
#  mp4_download_and_write_convert(mp4_url, "toto")
#  mp4_dowload_and_direct_convert(mp4_url, "toto")

  liste = theme_page_extract("filename.html")
  for i in range((len(liste))):
    print(liste[i][2])
    mp4_download_write_and_convert(liste[i][1], liste[i][2])

  

if __name__ == "__main__":
      main()
