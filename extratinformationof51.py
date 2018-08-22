# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:29:23 2018

@author: eddy
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://www.51job.com/")

#input query key words
elem = driver.find_element_by_id("kwdselectid")
#clear query words
elem.clear()
elem.send_keys("python")

#open city form
cityname = driver.find_element_by_id("work_position_input")
cityname.click()


#clear out all selection on cities
while(1):
    try:
        cityselected = driver.find_element_by_class_name("ttag")
    except:
        #print("find city finished")
        break
    else:
        cityselected.click()
        
    
#choose hangzhou as default city
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
driver.find_element_by_id("work_position_click_bottom_save").click()

elem.send_keys(Keys.RETURN)

#pospone for 3s
time.sleep(3)


try:
    context1 = driver.find_element_by_css_selector("#resultList")
except:
    print("end of list")
else:
    textarr = context1.text.split('\n')
    
#output controller
del textarr[0:11]
i = 1
while(i):
    if(textarr[i] == '上一页'):
        break
    print(textarr[i], end='')
    if(i%5):
        print("|", end='')
    else:
        print("")
    i = i+1

driver.close()