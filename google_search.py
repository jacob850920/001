# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:50:56 2020

@author: chenlw
"""
import csv
import requests
import pandas as pf
from io import StringIO
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import sys

print('\n\n\n需有Chrome瀏覽器才能執行此程式!!!')

url = "https://www.google.com.tw/"
#key_word=input('請輸入查詢關鍵字：')
#key_word="爬蟲 'edu.tw'"
# key_word="樂透 'edu.tw'"
# key_word="樂透 python 'edu.tw'"
key_word="陸軍官校 "

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'referer': 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID=2891'
}

options = webdriver.ChromeOptions()                                     #新增，略過網頁憑證錯誤
options.add_argument('--ignore-certificate-errors')                     #新增，略過網頁憑證錯誤
options.add_argument('user-agent-{}'.format(headers))                     #新增，略過網頁憑證錯誤
driver = webdriver.Chrome(chrome_options=options)                       #新增，略過網頁憑證錯誤

######################################################################
#resp = requests.post(url, headers=headers)
#
#resp.encoding = 'utf-8'
####################################################################
driver.get(url)
driver.find_element_by_name("q").click()
driver.find_element_by_name("q").clear()
driver.find_element_by_name("q").send_keys(key_word)
driver.find_element_by_id("tsf").submit()


# page=0
# with open('google_search3333.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
#     writer = csv.writer(csvfile)
#     writer.writerow(('標題','概述'))
#     writer.writerow(['連結'])

#     for i in range(8):
#         page+=1
#         html = driver.page_source
#         sp=BeautifulSoup(html,"html.parser")
#         search_h3=sp.select("div.yuRUbf > a > h3")
#         search_a=sp.select("div.yuRUbf > a")
#         search_span=sp.select("div.IsZvec > div > span.aCOpRe")
        
#         for i in range(len(search_h3)):
#             print(page)
#             print(search_h3[i].text,end=' ')
#             print(search_a[i].get('href'))
#             print(search_span[i].text)

#             writer.writerow([search_h3[i].text,search_span[i].text])
#             writer.writerow([search_a[i].get('href')])
    
#         driver.find_element_by_xpath("//a[@id='pnnext']/span[2]").click()
#         sleep(1)  # 必須加入等待，否則會有誤動作



# driver.close()               #關閉瀏覽器


# sys.exit

