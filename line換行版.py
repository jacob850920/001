# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:39:01 2020

@author: cis-user
"""

from selenium import webdriver
import csv


import sys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests

url="https://www.ettoday.net/news/news-list.htm"
options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)


for i in range(1):
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_h3=sp.select("div.part_list_2 > h3 > a")#標題跟網址用
    headers = {"Authorization": "Bearer " + "19DKXJkMJko0v3WBUhOni9qgQXKLWlCK1SG6pkkc0JD","Content-Type": "application/x-www-form-urlencoded"}

    params = {"message":search_h3[i].text +"\n" +"https://www.ettoday.net" +search_h3[i].get('href')}
    r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
    print(i)

driver.close()               #關閉瀏覽器


sys.exit   