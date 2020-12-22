# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:15:48 2020

@author: 90053
"""
from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import time,datetime
import sys
from selenium.webdriver.support.ui import Select
import requests


key="switch主機"
url="https://shopee.tw/search?keyword="+key
options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)

time.sleep(3)

page=0
with open('蝦皮爬蟲.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('商品名','網站','價格','連結'))
    
    

    for i in range(1):   
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_name=sp.select("div._1NoI8_")#商品名
        search_price=sp.select("div._1w9jLI > span._341bF0")#價格
        search_url=sp.select("div.col-xs-2-4 > div > a")#網址
        
        for i in range(15):  
                print(page)
                print(search_name[i].text,end=' ')
                print(search_price[i].text)
                print("https://shopee.tw" + search_url[i].get('href'))
                
            
                writer.writerow([search_name[i].text,"蝦皮購物",search_price[i].text,"https://shopee.tw"+search_url[i].get('href')])
                
driver.close()               #關閉瀏覽器


sys.exit                              
