# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:22:56 2020

@author: USER
"""

from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import time,datetime
import sys
from selenium.webdriver.support.ui import Select




key="switch"
url="https://tw.search.mall.yahoo.com/search/mall/product?kw="+key+"&p=iphone12mini64g&cid=hp&clv=0"
options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)


with open('YAHOO超級商城爬蟲.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('商品名','網站','價格','連結'))
    
    

    
       
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("div.main> div> ul > li> a > div >span> span.BaseGridItem__title___2HWui")#商品名
    search_price=sp.find_all("em")#價格
    search_url=sp.select("div.main> div> ul > li> a")
        
    for i in range(len(search_name)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[YAHOO超級商城]",end=' ')
        print(search_price[i].text,end=' ')
        print(search_url[i].get('href'))
                
            
        writer.writerow([search_name[i].text,"YAHOO超級商城",search_price[i].text,search_url[i].get('href')])
                
driver.close()               #關閉瀏覽器


sys.exit    