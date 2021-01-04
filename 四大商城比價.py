# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 08:12:03 2020

@author: 90053
"""

from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import sys
from selenium.webdriver.support.ui import Select
import time,datetime

with open('四大商城爬蟲.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('商品名','網站','價格','連結'))
    
    key="iphone 12 mini 64g"
    
    url="https://www.momoshop.com.tw/"
    options=webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver=webdriver.Chrome(chrome_options=options)
    # driver.get(url)
    
    driver.get("https://www.momoshop.com.tw/main/Main.jsp?mdiv=1099800000-bt_0_243_01-bt_0_243_01_e1&ctype=B")
    driver.find_element_by_id("keyword").click()
    driver.find_element_by_id("keyword").clear()
    driver.find_element_by_id("keyword").send_keys(key)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("div.prdInfoWrap > h3")#商品名
    search_price=sp.select("div.prdInfoWrap > p > span > b")#價格
    search_url=sp.select("div.listArea > ul > li > a")
    
    print("[MOMO購物網]")
    for i in range(len(search_name)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[MOMO購物網]",end=' ')
        a=search_price[i].text
        c=a.replace(',', '')
        print(search_price[i].text,end=' ')
        print("https://www.momoshop.com.tw"+search_url[i].get('href'))
        writer.writerow([search_name[i].text,"MOMO購物網",c,"https://www.momoshop.com.tw"+search_url[i].get('href')])
        
    print("[PChome線上購物]")
    url="https://shopping.pchome.com.tw/"
    driver.get(url)

    time.sleep(3)

    driver.get("https://shopping.pchome.com.tw/")
    driver.find_element_by_id("keyword").click()
    driver.find_element_by_id("keyword").clear()
    driver.find_element_by_id("keyword").send_keys(key)
    driver.find_element_by_id("doSearch").click()
    # driver.find_element_by_link_text(u"精準度").click()

    time.sleep(3)
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("div.Cm_C > dl > dd > h5 > a ")#商品名
    search_price=sp.select("div.Cm_C > dl > dd > ul > li > span > span")#價格
    search_url=sp.select("div.Cm_C > dl > dd > h5 > a ")#網址
        
    for i in range(len(search_name)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[PChome線上購物]",end=' ')
        print(search_price[i].text,end=' ')
        print("https:"+search_url[i].get('href'))
                
            
        writer.writerow([search_name[i].text,"PChome線上購物",search_price[i].text,"https:"+search_url[i].get('href')])
                
    print("[蝦皮商城]")
    url="https://shopee.tw/mall/search?keyword="+key
    driver.get(url)

    time.sleep(3)
    
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("div._1NoI8_")#商品名
    search_price=sp.find_all("div", class_="_1w9jLI _37ge-4 _2ZYSiu")#價格
    search_url=sp.select("div.col-xs-2-4 > div > a")#網址
        
    for i in range(len(search_name)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[蝦皮商城]",end=' ')
        a=search_price[i].text
        b=a.replace('$', '')
        c=b.replace(',', '')
        d=str(c).split( )[0]
        print("https://shopee.tw" + search_url[i].get('href'))
        
        
        writer.writerow([search_name[i].text,"蝦皮商城",d,"https://shopee.tw"+search_url[i].get('href')])
    print("[YAHOO超級商城]")
    url="https://tw.search.mall.yahoo.com/search/mall/product?kw="+key+"&p=iphone12mini64g&cid=hp&clv=0"
    driver.get(url)
    
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("div.main> div> ul > li> a > div >span> span.BaseGridItem__title___2HWui")#商品名
    search_price=sp.find_all("em")#價格
    search_url=sp.select("div.main> div> ul > li> a")
        
    for i in range(len(search_price)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[YAHOO超級商城]",end=' ')
        a=search_price[i].text
        b=a.replace('$', '')
        c=b.replace(',', '')
        print(search_url[i].get('href'))
                
            
        writer.writerow([search_name[i].text,"YAHOO超級商城",c,search_url[i].get('href')])
    driver.close()               #關閉瀏覽器

sys.exit