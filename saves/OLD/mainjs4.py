import cfscrape
import requests
from bs4 import BeautifulSoup as soup

url = "https://www.off---white.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20180101 Firefox/47.0",
    "Referer" : url
}
session = requests.session()
scraper = cfscrape.create_scraper(sess=session)
link = 'https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship'
r = scraper.get(link, headers=headers)
page = soup(r.text, "html.parser")
print(page)
