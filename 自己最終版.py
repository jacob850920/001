# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:50:12 2020

@author: USER
"""

from selenium import webdriver
import csv
import requests
from bs4 import BeautifulSoup
import time
import sys
from selenium.webdriver.support.ui import Select

url="https://www.ettoday.net/news/news-list.htm"

options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)




page=0
with open('google_search3333.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('標題','時間'))

    for i in range(2):
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_h3=sp.select("div.part_list_2 > h3 > a")#標題
        search_a=sp.select("div.part_list_2 > h3 > span")#時間
       
        
        for i in range(5):
            print(page)
            print(search_h3[i].text,end=' ')
            print(search_a[i].text)
            
            writer.writerow([search_h3[i].text,search_a[i].text])
           

           

    
        driver.find_element_by_id("selD").click()
        Select(driver.find_element_by_id("selD")).select_by_visible_text("5")
        driver.find_element_by_id("selD").click()
        driver.find_element_by_id("button").click()
        time.sleep(1)  # 必須加入等待，否則會有誤動作
    
driver.close()               #關閉瀏覽器


sys.exit    