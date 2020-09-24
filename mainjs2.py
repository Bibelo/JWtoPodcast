from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options)

browser.get('http://selenium.dev/')

#r = session.get('http://python-requests.org')

#r.html.render()
#print(r.text)

#result = session.run(get_jw)
# print(result)
#s.html.render()
#print(s.text)
