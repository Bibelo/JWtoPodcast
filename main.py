# v0.1
#
# To do
# Implememt config.ini containing URL of media categories

#import moviepy
#import io
#import moviepy.editor as mpy
#import xml.etree.ElementTree as ET

import datetime
import os
import hashlib
import json
from moviepy.editor import *
from lxml import etree as ET

import requests

def theme_page_download(url, html_output):
    # Download the page containing the index of all MP4 videos
    new_index = requests.get(url)
    new_index_content = new_index.text
    new_hash = hashlib.sha256(new_index_content.encode('utf-8')).hexdigest()

    # Has a previous page ever been downloaded?
    if os.path.exists(html_output):
        previous_index = open(html_output, 'r')
        previous_index_content = previous_index.read()
        previous_index.close()
        previous_hash = hashlib.sha256(previous_index_content.encode('utf-8')).hexdigest()

        # In this case, we compare the old index and the new index (with their hashes)
        if new_hash == previous_hash:
            print("index has not changed")
            return
        else:
            print("index has been updated")
            previous_index_write = open(html_output, 'w')
            previous_index_write.write(new_index_content)
            previous_index_write.close()
    else:
        print("index did not exist and has been created")
        new_file = open(html_output, 'w')
        new_file.write(new_index_content)
        new_file.close()


# def theme_page_download(url, html_output):
#  r = requests.get(url)

#  with open(html_output, 'wb') as f:
#    f.write(r.content)

def theme_page_extract(html_input):
  with open(html_input, 'r') as f:
    j = json.load(f)

    media_liste = []

    for i in range(len(j['category']['media'])):
      title = j['category']['media'][i]['title']
      media_url = j['category']['media'][i]['files'][0]['progressiveDownloadURL']
      media_filename = media_url.split('/')[-1][:-4]
      media_pubDate = j['category']['media'][i]['firstPublished']
      media_thumbnail = j['category']['media'][i]['images']['sqr']['sm']

      media_liste.append([title, media_url, media_filename, media_pubDate, media_thumbnail])

    return media_liste

# def mp4_download_write_and_convert(mp4_url, mp4_output):
#   s = requests.get(mp4_url)

#   with open(mp4_output+".mp4", 'wb') as f:
#     f.write(s.content)
#     video = VideoFileClip(mp4_output+".mp4")
#     video.audio.write_audiofile(mp4_output+".mp3")

#   media_length = os.path.getsize(mp4_output+".mp3")

# #  print("Size (or Length) of file is : ", media_length)

#   return media_length

# def mp4_dowload_and_direct_convert(mp4_url, mp4_output):
# # Work In Progress: find a way to avoid saving the mp4
#   t = requests.get(mp4_url)

# #  inmemoryfile = io.BytesIO(t.content)

#   #video = VideoFileClip(mp4_output+".mp4")
#   #video.audio.write_audiofile(mp4_output+".mp3")

#   video = mpy.VideoClip(t.content)
#   video.audio.write_audiofile(mp4_output+".mp3")

def xml_write(xml_basis_file, liste, xml_output_file):
  print(liste[4])
  tree = ET.XMLParser(remove_blank_text=True)
  root = ET.parse(xml_basis_file, tree).getroot()
  for i in range(len(liste)):
    title = liste[i][0]
    description = liste[i][0]
    link = liste[i][1]
    image_link = liste[i][4]
    length = liste[i][5]
    guid = liste[i][2]
    media_date = datetime.datetime.strptime(liste[i][3], '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%b %d, %Y")

    item = ET.Element("item")

    item_title = ET.SubElement(item, "title")
    item_title.text = title

    item_description = ET.SubElement(item, "description")
    item_description.text = description
    
    item_link = ET.SubElement(item, "link")
    item_link.text = link
    
    item_enclosure = ET.SubElement(item, "enclosure")
    
    item_enclosure.set("length", length)
    item_enclosure.set("type", "audio/mpeg")
    item_enclosure.set("url", link)
    
    item_pubDate = ET.SubElement(item, "pubDate")
    item_pubDate.text = media_date

#    For future addition to make it iphone compatible
#    OR to have a picture for each element?
#    item_itunes_author = ET.SubElement(item, "{itunes}author")
#    item_itunes_author.text = "Author Name"
#    item_itunes_duration = ET.SubElement(item, "{itunes}duration")
#    item_itunes_duration.text = "00:32:16"
#    item_itunes_explicit = ET.SubElement(item, "{itunes}explicit")
#    item_itunes_explicit.text = "no"
      
    item_guid = ET.SubElement(item, "guid")
    item_guid.text = guid
  
    # the new item is added under the channel section
    for channel in root.iter('channel'):
      channel.append(item)

  tree = ET.ElementTree(root)
  tree.write(xml_output_file, encoding='utf-8', pretty_print=True, xml_declaration=True)

#  ET.dump(root)

def main():
  morning_worship_URL = 'https://b.jw-cdn.org/apis/mediator/v1/categories/E/VODPgmEvtMorningWorship'
  morning_worship_file = morning_worship_URL.rsplit('/', 1)[-1]
  morning_worship_name = 'podcast_mw.xml'

  theme_page_download(morning_worship_URL, morning_worship_file)

#  open the previous URL with https://jsoneditoronline.org/
#
#  mp4_url="https://download-a.akamaihd.net/files/media_periodical/f7/jwbmw_E_201410_03_r240p.mp4"
#  theme_page_download("filename.html")
#  mp4_download_and_write_convert(mp4_url, "toto")
#  mp4_dowload_and_direct_convert(mp4_url, "toto")
# SAVE THIS PART IN GITLAB SNIPPETS
# https://github.com/JennieJi/vsext-gitlab-snippets

  liste = theme_page_extract(morning_worship_file)
#  print(liste[2])
  for i in range((len(liste))):
  #for i in range(2):
    #media_length = mp4_download_write_and_convert(liste[i][1], liste[i][2])
    #media_length = str(os.path.getsize(liste[i][2]+".mp3"))

    # the following is temporary: all mp4s need to be downloaded and converted to mp3s...
    media_length = "1024"
    # print(type(file_length))
    liste[i].append(media_length)
    #print(liste[i])
  #xml_write("podcast2.xml", liste[i][0], liste[i][0], liste[i][1], liste[i][1], liste[i][4])
  
  xml_write("podcast_ref.xml", liste, morning_worship_name)
#   xml_write("podcast_ref.xml", liste, "podcast.xml")

  os.system("mv " + morning_worship_name + " /var/www/podcast")

if __name__ == "__main__":
      main()
