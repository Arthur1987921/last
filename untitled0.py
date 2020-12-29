# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:44:53 2020

@author: nan
"""

from selenium import webdriver
import csv
import requests
from bs4 import BeautifulSoup
import time,datetime
import sys
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get("https://www.google.com.tw/")
driver.find_element_by_name("q").click()
driver.find_element_by_name("q").clear()
driver.find_element_by_name("q").send_keys(u"台南市美食")
driver.find_element_by_id("tsf").submit()
driver.find_element_by_xpath("//div[@id='rso']/div/div/div[2]/div/div[6]/div/g-more-link/a/div/span[2]").click()
driver.find_element_by_xpath("//div[@id='rl_ist0']/div[1]/div[4]/div[1]/div").click()
page=0
with open('抓五天新聞.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('店名','星數','評論數','營業時間','地區'))
    
    for i in range(10):
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_h3=sp.select("div.dbg0pd")#店名
        search_a=sp.select("span.BTtC6e")#星星
        search_b=sp.select("span.rllt__wrapped")#營業時間
        search_c=sp.select("span > div:nth-child(1) > span:nth-child(3)")#評論數
        search_d=sp.select("span > div:nth-child(2)")#地區
        
        
        print(page)
        print(search_h3[i].text,end=' ')
        print(search_a[i].text,end=' ')
        print(search_b[i].text,end=' ')
        print(search_c[i].text,end=' ')
        print(search_d[i].text,end=' ')
        print(search_h3[i].get('href'))#抓網址
            
        writer.writerow([search_h3[i].text,search_a[i].text,search_c[i].text,search_b[i].text,search_d[i].text])
            
       
        
        time.sleep(2)  #動作太快會出錯,所以要加入等待時間
    
driver.close()               #關閉瀏覽器


sys.exit   




# driver.find_element_by_xpath("//div[@id='rso']/div/div/div[2]/div/div[6]/div/g-more-link/a/div/span[2]").click()
 