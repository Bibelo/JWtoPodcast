from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get("https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
