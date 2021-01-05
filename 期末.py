# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 08:24:59 2021

@author: nan
"""

import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sys
import time,datetime

url = 'https://www.google.com.tw/maps/@22.6258207,120.3437568,14z'
key_word = '高雄市美食'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=options)
#options.add_argument('user-agent-[]'.format(headers))
driver.get(url)

driver.find_element_by_id("searchboxinput").click()
driver.find_element_by_id("searchboxinput").clear()
driver.find_element_by_id("searchboxinput").send_keys(key_word)
driver.find_element_by_id("searchbox-searchbutton").click()
time.sleep(5)
################下拉#######################
# scrollable_div = driver.find_element_by_css_selector('div.section-layout.section-scrollbox.scrollable-y.scrollable-show.section-layout-flex-vertical')
# driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
###########################################




page=0
with open('gooloe評論123.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('店名','星數','評論數','地區','營業狀態','路線'))
    list1=[]

    for i in range(2):
        for j in range(10): #選取則數
            driver.find_element_by_xpath("//div[@id='pane']/div/div/div/div/div/div/a["+str(j+1)+"]").click()
            time.sleep(3)
            html = driver.page_source
            sp=BeautifulSoup(html,"html.parser")
            time.sleep(3)
            search_a=sp.select("div.section-hero-header-title-description > div:nth-child(1) > h1")#名稱
            search_star=sp.select("div.reviews-tap-area.reviews-tap-area-enabled > span > span")#星數
            search_com=sp.select("span.reviews-tap-area.reviews-tap-area-enabled > span:nth-child(1)")#評論數
            search_religion=sp.select("div.ugiz4pqJLAG__content > div.ugiz4pqJLAG__text")#地區
            try:
                search_open=sp.select("div > div.cX2WmPgCkHi__primary-text")#營業狀態
            except:
                print("查無營業時間")
            search_map=sp.select("div.section-hero-header-title-description > div:nth-child(1) > h1")#路線
            # try:
            #     search_cel=sp.select("div.widget-pane-content.scrollable-y > div > div > div:nth-child(16) > button > div.ugiz4pqJLAG__content > div.ugiz4pqJLAG__text > div.ugiz4pqJLAG__primary-text.gm2-body-2")#電話
            # except:
            #     search_cel=sp.select("div.widget-pane-content.scrollable-y > div > div > div:nth-child(13) > button > div.ugiz4pqJLAG__content > div.ugiz4pqJLAG__text > div.ugiz4pqJLAG__primary-text.gm2-body-2")#電話
            
            for j in range(len(search_a)):
                try:
                    list1.append(["[店名]：",search_a[j].text,"[星數]：",search_star[j].text,"[評論數]：",search_com[j].text,"[地區]:",search_religion[j].text,"[營業時間]：",search_open[j].text,"[路線]：https://www.google.com.tw/maps/place/",search_map[j].text])
                except:
                    list1.append(["[店名]：",search_a[j].text,"[星數]：",search_star[j].text,"[評論數]：",search_com[j].text,"[地區]:",search_religion[j].text,"[營業時間]：",'查無營業時間',"[路線]：https://www.google.com.tw/maps/place/",search_map[j].text])
                
            
            driver.find_element_by_xpath("//div[@id='pane']/div/div/div/div/button").click()
            
            time.sleep(3)
        driver.find_element_by_xpath("//button[@id='n7lv7yjyC35__section-pagination-button-next']/img").click()
        time.sleep(3)
    list1.sort(key=lambda s: float(s[3]), reverse=True)
    for i in range(len(list1)): 
        print(str(list1[i][0]+list1[i][1]))
        print(str(list1[i][2]+list1[i][3]))
        print(str(list1[i][4]+list1[i][5]))
        print(str(list1[i][6]+list1[i][7]))
        print(str(list1[i][8]+list1[i][9]))
        print(str(list1[i][10]+list1[i][11])+'\n')
    for i in range(len(list1)): 
        writer.writerow([list1[i][1],list1[i][3],list1[i][5],list1[i][7],list1[i][9],list1[i][10]+list1[i][11]])
    
    #     headers = {"Authorization": "Bearer " + "Le4CPxXLtPH0WiyJ8CrixPdHzal52R2M03ghQL6DmNK",
    #                 "Content-Type": "application/x-www-form-urlencoded"}
    #     params = {"message":['\n'+list1[i][0]+list1[i][1]+'\n'+
    #                           list1[i][2]+list1[i][3]+'\n'+
    #                           list1[i][4]+list1[i][5]+'\n'+
    #                           list1[i][6]+list1[i][7]+'\n'+
    #                           list1[i][8]+list1[i][9]+'\n'+
    #                           list1[i][10]+list1[i][11]]}
    #     r = requests.post("https://notify-api.line.me/api/notify",
    #                       headers=headers, params=params)
    # print(r.status_code)  #200