# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:13:24 2020

@author: 90053
"""

from selenium import webdriver
import csv
import requests
from bs4 import BeautifulSoup
import time
url="https://www.google.com/"
key_word="kobe"
options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)
driver.find_element_by_name("q").click()
driver.find_element_by_name("q").clear()
driver.find_element_by_name("q").send_keys(key_word)
driver.find_element_by_id("tsf").submit()

page=0
with open('google_search3333.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('標題','概述',"連結"))


    for i in range(8):
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_h3=sp.select("div.yuRUbf > c1 > c8")
        search_a=sp.select("div.yuRUbf > a")
        search_span=sp.select("div.IsZvec > div > span.aCOpRe")
        
        for i in range(len(search_h3)):
            print(page)
            print(search_h3[i].text,end=' ')
            print(search_a[i].get('href'))
            print(search_span[i].text)

            writer.writerow([search_h3[i].text,search_span[i].text])
            writer.writerow([search_a[i].get('href')])
    
        driver.find_element_by_xpath("//a[@id='pnnext']/span[2]").click()
        time.sleep(1)  # 必須加入等待，否則會有誤動作