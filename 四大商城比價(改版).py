# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:18:08 2021

@author: cis-user
"""

from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import sys
from selenium.webdriver.support.ui import Select
import time,datetime

search_list=[]

with open('四大商城爬蟲.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('商品名','價格','網站','連結'))
    
    key="iphone12"
    
    url="https://www.momoshop.com.tw/main/Main.jsp"
    options=webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver=webdriver.Chrome(chrome_options=options)
    driver.get(url)
    driver.find_element_by_id("keyword").click()
    driver.find_element_by_id("keyword").clear()
    driver.find_element_by_id("keyword").send_keys(key)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    
    time.sleep(3)
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
        search_list.append([search_name[i].text,c,"MOMO購物網","https://www.momoshop.com.tw"+search_url[i].get('href')])
        
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
                
        search_list.append([search_name[i].text,search_price[i].text,"PChome線上購物","https:"+search_url[i].get('href')])
                
    print("[蝦皮商城]")
    url="https://shopee.tw/mall/search?keyword="+key
    driver.get(url)

    time.sleep(10)
    
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.select("div._1NoI8_")#商品名
    search_price=sp.find_all("div", class_="_1w9jLI _1DGuEV _7uLl65")#價格
    search_url=sp.select("div.col-xs-2-4 > a")#網址
        
    for i in range(len(search_name)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[蝦皮商城]",end=' ')
        a=search_price[i].text
        b=a.replace('$', '')
        c=b.replace(',', '')
        d=str(c).split( )[0]
        print(search_price[i].text)
        print("https://shopee.tw/" + search_url[i].get('href'))
        
        search_list.append([search_name[i].text,d,"蝦皮商城","https://shopee.tw/"+search_url[i].get('href')])
    print("[YAHOO超級商城]")
    
    
    url="https://tw.mall.yahoo.com/search/product?p="+key
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    search_name=sp.find_all("span", class_="BaseGridItem__title___2HWui")#商品名
    search_price=sp.find_all("em")#價格
    search_url=sp.find_all("a")
        
    for i in range(len(search_price)):  
        print(i+1)
        print(search_name[i].text,end=' ')
        print("[YAHOO超級商城]",end=' ')
        a=search_price[i].text
        b=a.replace('$', '')
        c=b.replace(',', '')
        print(search_price[i].text)
        print(search_url[i].get('href'))
        search_list.append([search_name[i].text,c,"YAHOO超級商城",search_url[i].get('href')])
       
    search_list.sort(key=lambda s: int(s[1]))  
    
    for i in range(len(search_list)): 
        writer.writerow([search_list[i][0],search_list[i][1],search_list[i][2],search_list[i][3]])
    
    
                
        
    driver.close()               #關閉瀏覽器

sys.exit