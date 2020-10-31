from selenium import webdriver

from bs4 import BeautifulSoup

#driver = webdriver.PhantomJS()

options = webdriver.ChromeOptions()
options.add_argument('--headless --no-sandbox')
options.add_argument('--no-sandbox')
options.add_argument('--headless --no-sandbox')

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=options)



jw_morningworship_url = 'https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship'
driver.get(jw_morningworship_url)

print(driver)

exit
html_text = requests.get(jw_morningworship_url).text
soup = BeautifulSoup(html_text, 'html.parser')

#jw_morningworship = open("jw.html", 'r')
#soup = BeautifulSoup(jw_morningworship, 'html.parser')

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

#articles = soup.find("article", {"id": "article"})
#print(articles)
for a in soup.find_all('a', href=True):
  print(a['href'])
