# Convert JW.ORG medias into an audio RSS Podcast

## Description

There's a wonderful pool of spiritual resources on JW.ORG.
This program makes it possible to follow them easily using the practical features of a podcast player.

This will create a channel for each main page containing media resources on JW.ORG.

## Quick installation

The file `default_config.ini` contains samples of the fields you need to add, especially the source for the medias.

- rename `default_config.ini` to `config.ini`
- run main.py (python3)
  - ```python3 main.py```
- you can add this line to your crontab to check for updates every week for example

The resulting URL will be `http(s)://<general_url>/<podcast_file>.xml`
The XML file being locally copied to `<general_local_path>`

Add this URL to your podcast player.
The podcast player will then read the MP4 video directly from JW.ORG as sounds.

**Tested successfully with Podcast Republic**

## Personal installation

To find new sources you'd like to add yourself, go to:
- JW.ORG / Library / Videos
- Click on one of the Video categories (Family, Programs and Events, etc.)
- Click on `See All` for one sub-category (Annual Meeting, Special Programs, etc.)
- Extract the JSON main index storing all the information for this page:
  - Right-click : Inspect (Chrome)
  - In Inspect, click on the Network tab
  - Reload the page
  - Find a `b.jw-cdn.org` page starting with `VOD` (hover over the filename to see the full URL of the resource)
    - Right-click then `Copy / Copy link address`
  - Click on that resource: it should contain a `category` section, containing a `media` section.
  - The `media` section contains a list of resources, with items like `title`, `firstPublished`, etc.
  - That's the page you want to add to `config.ini`, in the `jw_url` field

## TODO

- maybe a module extracting the VOD JSON index from the public JW.ORG page
