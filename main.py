#v0.9 Bibelo 10th of Nov, 2020


import datetime
import hashlib
import json
import os
import requests
from configparser import ConfigParser
from lxml import etree as ET

def init():
  global ini_config_file, basis_xml_file, website_path, resources_path
  ini_config_file = 'config.ini'
  basis_xml_file = 'podcast_ref.xml'
  website_path = '/var/www/podcast'
  resources_path = 'resources'

def theme_page_download(jw_url, podcast_html_file):
    # Download the page containing the index of all MP4 videos
    print("Downloading the JW media index")
    new_index = requests.get(jw_url)
    new_index_content = new_index.text
    new_hash = hashlib.sha256(new_index_content.encode('utf-8')).hexdigest()

    # Has a previous page ever been downloaded?
    if os.path.exists(podcast_html_file):
        previous_index = open(podcast_html_file, 'r')
        previous_index_content = previous_index.read()
        previous_index.close()
        previous_hash = hashlib.sha256(previous_index_content.encode('utf-8')).hexdigest()

        # In this case, we compare the old index and the new index (with their hashes)
        if new_hash == previous_hash:
            print("JW media index has not been updated on jw.org")
            return
        else:
            print("JW media index has been updated on jw.org")
            previous_index_write = open(podcast_html_file, 'w')
            previous_index_write.write(new_index_content)
            previous_index_write.close()
    else:
        print("A local index did not exist and has been created")
        new_file = open(podcast_html_file, 'w')
        new_file.write(new_index_content)
        new_file.close()

def theme_page_extract(podcast_html_file):
  with open(podcast_html_file, 'r') as f:
    json_index = json.load(f)

    podcast_fields = []

    for i in range(len(json_index['category']['media'])):
      title = json_index['category']['media'][i]['title']
      media_url = json_index['category']['media'][i]['files'][0]['progressiveDownloadURL']
      media_filename = media_url.split('/')[-1][:-4]
      media_pubDate = json_index['category']['media'][i]['firstPublished']
      # media_thumbnail = json_index['category']['media'][i]['images']['sqr']['sm']

      # podcast_fields.append([title, media_url, media_filename, media_pubDate, media_thumbnail])
      podcast_fields.append([title, media_url, media_filename, media_pubDate, None])

    return podcast_fields

def xml_write(xml_basis_file, podcast_fields, general_parameters, podcast_parameters):
  general_title = general_parameters[0]
  general_url = general_parameters[1]
  general_description = general_parameters[2]

  podcast_name = podcast_parameters[0]
  podcast_file = podcast_parameters[1]
  podcast_logo_filename = podcast_parameters[2]

  # Print the first episode title, to make sure it works
  # print(podcast_fields[4])

  tree = ET.XMLParser(remove_blank_text=True)
  root = ET.parse(xml_basis_file, tree).getroot()
  
  # <title> of the Podcast
  root[0][0].text = general_title + " " + podcast_name
  # <link> URL of the Podcast
  root[0][1].text = general_url + podcast_file
  # <description> of the Podcast
  root[0][3].text = general_description + " " + podcast_name
  # <image><url> URL of the image of the Podcast
  root[0][4][0].text = general_url + podcast_logo_filename
  # <image><title> Title of the logo
  root[0][4][1].text = podcast_name
  # <image><link> = URL of the Podcast
  root[0][4][2].text = general_url + podcast_file

  print("Generating XML for Podcast " + root[0][0].text)
  print(root[0][1].text)
  
  for i in range(len(podcast_fields)):
    title = podcast_fields[i][0]
    description = podcast_fields[i][0]
    link = podcast_fields[i][1]
    image_link = podcast_fields[i][4]
    length = podcast_fields[i][5]
    guid = podcast_fields[i][2]
    media_date = datetime.datetime.strptime(podcast_fields[i][3], '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%b %d, %Y")

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
  tree.write(podcast_file, encoding='utf-8', pretty_print=True, xml_declaration=True)

  # ET.dump(root)

def main():
  init()

  ini_config = ConfigParser()
  ini_config.read(ini_config_file)

  general_title = ini_config['General']['general_title']
  general_url = ini_config['General']['general_url']
  general_description = ini_config['General']['general_description']
  general_local_path = ini_config['General']['general_local_path']
  general_parameters = [general_title, general_url, general_description]

  for section in ini_config.sections():
    if section == 'General':
      continue

    jw_url = ini_config[section]['jw_url']
    podcast_name = ini_config[section]['podcast_name']
    podcast_xml_file = ini_config[section]['podcast_file'] + ".xml"
    podcast_html_file = ini_config[section]['podcast_file'] + ".html"
    podcast_logo_filename = ini_config[section]['podcast_logo_filename']

    podcast_parameters = [podcast_name, podcast_xml_file, podcast_logo_filename]

    print("For podcast " + podcast_name)

    theme_page_download(jw_url, podcast_html_file)

    # Extract the different fields from the index and put them in list
    podcast_fields = theme_page_extract(podcast_html_file)

    # here, we just add the length
    for i in range((len(podcast_fields))):
      media_length = "1024"
      podcast_fields[i].append(media_length)

    # Creation of the whole XML file!  
    xml_write(basis_xml_file, podcast_fields, general_parameters, podcast_parameters)

    print("Copying XML Podcast file and logo for " + podcast_name)
    print("Copying to " + general_local_path + "\n")
    os.system("mv " + podcast_xml_file + " " + general_local_path)
    os.system('cp ' + resources_path + "/" + podcast_logo_filename + " " + general_local_path)

if __name__ == "__main__":
      main()
