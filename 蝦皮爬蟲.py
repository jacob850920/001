# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:44:12 2020

@author: USER
"""

from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import time,datetime
import sys
from selenium.webdriver.support.ui import Select
import requests


key="iphone 12 mini 64g"
url="https://shopee.tw/mall/search?keyword="+key
options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)

time.sleep(3)


with open('蝦皮爬蟲.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('商品名','網站','價格','連結'))
    
    

      
        
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("div._1NoI8_")#商品名
    search_price=sp.find_all("div", class_="_1w9jLI _37ge-4 _2ZYSiu")#價格
    search_url=sp.select("div.col-xs-2-4 > div > a")#網址
        
    for i in range(len(search_name)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[蝦皮商城]",end=' ')
        print(search_price[i].text,end=' ')
        print("https://shopee.tw" + search_url[i].get('href'))
                
            
        writer.writerow([search_name[i].text,"蝦皮商城",search_price[i].text,"https://shopee.tw"+search_url[i].get('href')])
                
driver.close()               #關閉瀏覽器


sys.exit 