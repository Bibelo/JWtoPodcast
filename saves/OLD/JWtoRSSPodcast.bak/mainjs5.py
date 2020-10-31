from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC 

import time
import sys

#url = 'https://www.brainyquote.com/'
url = "https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship"
#chrome_driver_path = '/Users/mahmud/Desktop/demopython/selenium_project/chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"')

webdriver = webdriver.Chrome(
  #executable_path=chrome_driver_path, options=chrome_options
  options=chrome_options
)

user_agent = webdriver.execute_script("return navigator.userAgent;")
print(user_agent)



# default search query
# search_query = "life"

# if (len(sys.argv) >= 2):
#  search_query = sys.argv[1]
#  print(search_query)


    # Set timeout time 
webdriver.get(url)
try: 
    # wait 10 seconds before looking for element 
    element = WebDriverWait(webdriver, 10).until( 
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "VIDE")) 
#        EC.element_to_be_clickable()
    ) 
finally: 
    # else quit 
    webdriver.quit() 

print(webdriver.page_source)
quit()

#WebDriverWait(webdriver, 200)

    # retrive url in headless browser
#webdriver.implicitly_wait(20)
  #  driver.maximize_window()

    #print(driver.page_source.encode("utf-8"))
    
    # find search box
 #   search = driver.find_element_by_id("hmSearch")
 #   search.send_keys(search_query + Keys.RETURN)
    
 #   wait.until(presence_of_element_located((By.ID, "quotesList")))
    # time.sleep(3)
#    results = driver.find_elements_by_class_name('m-brick')
print(webdriver.page_source)

#    for quote in results:
#      quoteArr = quote.text.split('\n')
#      print(quoteArr)
#      print()

    # must close the driver after task finished
webdriver.close()
