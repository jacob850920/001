# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:42:30 2020

@author: USER
"""

from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import time,datetime
import sys
from selenium.webdriver.support.ui import Select




key="iphone 12 mini 64g"
url="https://www.momoshop.com.tw/"
options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)



driver.get("https://www.momoshop.com.tw/main/Main.jsp?mdiv=1099800000-bt_0_243_01-bt_0_243_01_e1&ctype=B")
driver.find_element_by_id("keyword").click()
driver.find_element_by_id("keyword").clear()
driver.find_element_by_id("keyword").send_keys(key)
driver.find_element_by_xpath("//button[@type='submit']").click()



with open('MOMO爬蟲.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('商品名','網站','價格','連結'))
    
    

    
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("div.prdInfoWrap > h3")#商品名
    search_price=sp.select("div.prdInfoWrap > p > span > b")#價格
    search_url=sp.select("div.listArea > ul > li > a")
        
    for i in range(len(search_name)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[MOMO購物網]",end=' ')
        print(search_price[i].text,end=' ')
        print("https://www.momoshop.com.tw"+search_url[i].get('href'))
        writer.writerow([search_name[i].text,"MOMO購物網",search_price[i].text,"https://www.momoshop.com.tw"+search_url[i].get('href')])
                
driver.close()               #關閉瀏覽器


sys.exit    