# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:03:43 2020

@author: 90053
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
a=time.strftime('%d' , time.localtime())




page=0
with open('抓五天新聞.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('標題','時間'))

    for i in range(5):
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_h3=sp.select("div.part_list_2 > h3 > a")#標題
        search_a=sp.select("div.part_list_2 > h3 > span")#時間
       
        
        for i in range(5):  #怕跑太久，每天先抓五個新聞
            print(page)
            print(search_h3[i].text,end=' ')
            print(search_a[i].text)
            
            writer.writerow([search_h3[i].text,search_a[i].text])
           

           

        a=int(a)-1
        a=str(a)
        driver.find_element_by_id("selD").click()
        Select(driver.find_element_by_id("selD")).select_by_visible_text(a)
        driver.find_element_by_id("selD").click()
        driver.find_element_by_id("button").click()
        time.sleep(1)  # 必須加入等待，否則會有誤動作
    
driver.close()               #關閉瀏覽器


sys.exit    