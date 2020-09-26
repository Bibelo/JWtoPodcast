import requests
from moviepy.editor import *
from bs4 import BeautifulSoup

#driver = webdriver.PhantomJS()


#jw_morningworship_url = 'https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship'
#session = dryscrape.Session()
#session.visit(jw_morningworship_url)

#print(driver)

#html_text = requests.get(jw_morningworship_url).text
#soup = BeautifulSoup(html_text, 'html.parser')

jw_morningworship = open("jw3.html", 'r')
soup = BeautifulSoup(jw_morningworship, 'html.parser')

#print(soup.find_all(attrs={"id": "article"}))
#print(soup.find_all("article"))
#print(soup.body)
#print(soup.body)
#print(soup.body.findChildren("article", {"id": "article"}))
#articles = soup.body.find_all("article", {"id": "article"})

#articles = soup.find("div", {"class": "synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en lang-E"})
#articles = soup.find("div", {"class": "synopsis"})
#articles = soup.find_all('class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en lang-E"')
#articles = soup.find_all('div class')

#print(articles)

#print(soup.find_all('a'))
#print(articles.find())

#print(soup.body.find(id="article"))

# article_id="article"
# contenu de a href balise

articles = soup.find("div", {"class": "dropdownBody"})
for a in articles.find_all('a', href=True):
  if a['href'].endswith('240p.mp4') == True:
    mp4_link = a['href']

print(mp4_link)
filename = mp4_link.split("/")[-1][:-4]

print(filename)

r = requests.get(mp4_link)
#open(filename+".mp4", 'wb').write(r.content)
video = VideoClip(r)
video.audio.write_audiofile(filename+".mp3")

quit()

r = requests.get(mp4_link)
open(filename+".mp4", 'wb').write(r.content)
video = VideoFileClip(filename+".mp4")
video.audio.write_audiofile(filename+".mp3")
# trouver moyen d'extraire le texte
