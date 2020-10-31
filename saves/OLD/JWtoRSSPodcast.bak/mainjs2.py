from selenium import webdriver
from selenium.webdriver.firefox.options import Options

profile = webdriver.FirefoxProfile()
#profile.set_preference("general.useragent.override", useragent.random)
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36")


options = Options()
options.headless = True

browser = webdriver.Firefox(firefox_profile=profile, options=options)
#browser = webdriver.Firefox(options=options)

#browser.get('http://selenium.dev/')
browser.get('https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship')

print(browser.page_source.encode("utf-8"))


#browser.html.render()
