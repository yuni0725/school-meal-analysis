from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

from time import sleep

import re

global drinks
drinks = [
    ["음 식 명", "중량(g)" ,"에너지(kcal)","탄수화물(g)","당류(g)","지방(g)",'단백질(g)','칼슘(mg)','인(mg)','나트륨(mg)','칼륨(mg)','마그네슘(mg)','철(mg)','아연(mg)','콜레스테롤(mg)','트랜스지방(g)']
]

URL = "https://www.mega-mgccoffee.com/menu/?menu_category1=1"

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(10)
driver.get(URL)

def get_drink():
    soup = BeautifulSoup(driver.page_source, "html.parser")

    menu_list = soup.find("ul", id="menu_list").find("ul", id="menu_list")

    lis = menu_list.find_all("li", recursive=False)

    for li in lis:
        text = li.find_all("div", "cont_text_inner")
        text_new = []
        for t in text:
            text_new.append(t.text.replace("\t", "").replace(" ", "").replace("\n", ""))
        name = text_new[0]
        if "/" in text_new[4]:
            weight = int(text_new[4].split("/")[1].split("o")[0]) * 29.5
        else:
            try:
                weight = int(text_new[4].split("o")[0]) * 29.5
            except:
                return
        weight = int(weight)
        kcal = text_new[5].split("k")[0].split("량")[1]


        lis = li.find("div", "cont_list_small2").find_all("li")
        if len(lis) == 5:
            del lis[4]

        for i in range(0, 4):
            text = lis[i].text.replace("\t", "").replace(" ", "").replace("\n", "")
            text = re.sub(r'[a-zA-Z가-힣]', '', text)

            if i == 0:
                fat = text
            elif i == 1:
                sugar = text
            elif i == 2:
                na = text
            elif i == 3:
                protein = text
        drink = [
            name, weight, kcal, 0, sugar, fat, protein, 0, 0, na, 0, 0, 0, 0, 0, 0
        ]

        if drink in drinks:
            pass
        else:
            drinks.append(drink)

sleep(2)
get_drink()

for i in [3, 5, 6, 7]:
    driver.find_element(By.XPATH, f'//*[@id="board_page"]/li[{i}]').click()
    sleep(2)
    get_drink()

for i in [4, 5]:
    driver.find_element(By.XPATH, f'//*[@id="board_page"]/li[{i}]').click()
    sleep(2)
    get_drink()

sleep(10)

driver.quit()

import csv

f = open("DB_drink_mega.csv", "w", newline="", encoding="UTF-8")
writer = csv.writer(f)

for d in drinks:
    writer.writerow(d)
f.close