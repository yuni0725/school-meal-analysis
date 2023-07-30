from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

URL = f"https://school.jbedu.kr/sangsan/M01060401/list?s_idx=1"

options = webdriver.ChromeOptions()
options.add_experimental_option(
    "prefs",
    { "download.default_directory": 'C:\\Users\\user\\Desktop\\Code\\menu',
      "download.prompt_for_download": False,   
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True
    }
)
options.add_argument('headless')

driver = webdriver.Chrome(options=options)

driver.get(URL)
driver.implicitly_wait(15)

for i in range(1, 11):
    driver.find_element(By.CSS_SELECTOR, f'#usm-content-body-id > table > tbody > tr:nth-child({i}) > td.tch-tit > a').click()
    driver.find_element(By.CSS_SELECTOR, '#m_mainView > tbody > tr:nth-child(3) > td > div > div.file-btn2 > span:nth-child(1) > a').click()
    driver.back()
    print("download complete")

print('Done!')

sleep(2)

driver.close()
driver.quit()

