import hashlib
import os
import requests

def theme_page_download(url, html_output):
    # Download the page with all MP4 videos
    new_index = requests.get(url)
    new_index_content = new_index.text
    
    new_hash = hashlib.sha256(new_index_content.encode('utf-8')).hexdigest()
    print("hash of new downloaded index: " + new_hash)

    # Has a previous page ever been downloaded?
    if os.path.exists(html_output):
        previous_index = open(html_output, 'r')
        previous_index_content = previous_index.read()
        previous_index.close()

        # In this case, we compare the old index and the new index (with their hashes)
        previous_hash = hashlib.sha256(previous_index_content.encode('utf-8')).hexdigest()
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

def main():
    theme_page_download('https://b.jw-cdn.org/apis/mediator/v1/categories/E/VODPgmEvtMorningWorship', 'filename.html')

if __name__ == "__main__":
      main()