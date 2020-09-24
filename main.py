from bs4 import BeautifulSoup

#driver = webdriver.PhantomJS()


#jw_morningworship_url = 'https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship'
#session = dryscrape.Session()
#session.visit(jw_morningworship_url)

#print(driver)

#html_text = requests.get(jw_morningworship_url).text
#soup = BeautifulSoup(html_text, 'html.parser')

jw_morningworship = open("jw2.html", 'r')
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

articles = soup.find("article", {"id": "article"})
for a in articles.find_all('a', href=True):
  print(a['href'])
