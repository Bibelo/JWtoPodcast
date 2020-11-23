# Convert JW.ORG medias into an audio RSS Podcast

## Description

There's a wonderful pool of spiritual resources on JW.ORG.
This program makes it possible to follow them easily using the practical features of a podcast player.

This will create a channel for each main page containing media resources on JW.ORG.

## Quick installation

The file `default_config.ini` contains samples of the fields you need to add, especially the source for the medias.

- rename `default_config.ini` to `config.ini`
- run main.py (python3)
```python3 main.py```
- you can add this line to your crontab to check for updates every week for example

The resulting URL will be `general_url`/`podcast_file`.xml
The XML file being locally copied to `general_local_path`

Add this URL to your podcast player.
The podcast player will then read the MP4 video directly from JW.ORG as sounds.

**Tested successfully with Podcast Republic**

## TODO

- move init global var to config.ini
- implement default_config.ini
- do not copy files if index has not been changed
- update README.md explaining how to create the podcast
