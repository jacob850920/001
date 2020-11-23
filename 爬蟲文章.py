# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:23:10 2020

@author: cis-user
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium .webdriver.support.ui import Select

# r = requests.get("https://udn.com/news/story/7321/5018383?from=udn_ch2_menu_v2_main_index")
r = requests.get("https://udn.com/news/story/6813/5020920")
r.encoding = "utf8"

with open('html.txt', "w", encoding="utf8") as fp:
    # print(r.text,file=fp)                                 ##可用print，也可用write
    fp.write(r.text)
    
with open('html.txt', "r", encoding="utf8") as fp2:
    r2=fp2.read() 
    
page_source = r.text
page_source2 = page_source.split('\n')

soup = BeautifulSoup(r.text, "lxml")

####################################老師第一種#######################################
# tag_div=soup.find_all('section',class_="article-content__wrapper")
# print(tag_div)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# for a in tag_div:
    
#     print(a.text.replace())


####################################老師第二種#######################################

# search_span=soup.select("body > main > div > section.wrapper-left.main-content__wrapper > section > article > div > section.article-content__editor")

# search_span2=soup.select("div > ul > li > a")


# print(soup.prettify())

# r.test.to_csv('GetAllStock.csv',encoding='utf-8-sig')

####################################自己的作業#######################################
tag_div=soup.find_all('div',class_="article-content__paragraph")
print(tag_div)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for a in tag_div:
    print(a.text)
    #寫入txt
    fp=open("text2.txt","w",encoding="utf-8")
    fp.write(a.text)
fp.close()


f = open("text2.txt")
# f = open("/Users/Administrator/Desktop/logs-160k/loss-160k/g_losses.txt")
line = f.readline()  #讀取一行
count = 0
count1=0
# print(line)
k = open("csv","a")
# k = open("/Users/Administrator/Desktop/logs-160k/loss-160k/g_losses_1.txt","a")
while line:
    count=count+1  #計算文字行數
    # print(count)
    if(count>21000):
        break
    if((count%1)==0):
      if (float(count)<10000):
          if (float(line)<0.1):
            k.write(" ")
            k.write("\n")
      if (float(count)>10000):
         if (float(line)<1):
            count1=count1+1
            line_prime=line
            line = 0.0
            line = str(line)
            k.write(" ")        # 寫入空格
            k.write("\n")       # 換行
            print("line_prime:",line_prime)
            print("line:",count,line)
            print("count1:",count1)
         elif (float(line)>8):
            line = 0.0
            line = str(line)
            k.write(" ")
            k.write("\n")
         else:
             k.write(line)
      else:
        k.write(line)
    line = f.readline()
    # print("line:",(line))
f.close()