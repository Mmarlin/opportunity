# Import required libraries

import time
import xlsxwriter
import openpyxl
import mysql.connector

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

# Defining the connection to the database

browser = webdriver.Chrome('C:\\Users\\marli\\Downloads\\chromedriver_win32\\chromedriver')
base_link = 'https://www.offcampusjobs4u.com/'

# Scroll to bottom of page for the data to load
def scroll_bottom():
    # Scroll down to the bottom of the page
    l=browser.find_element_by_xpath("//*[contains(text(), 'Made with')]")
    # action object creation to scroll
    a = ActionChains(browser)
    a.move_to_element(l).perform()
    sleep(5)

total =[]
browser.get(base_link)
scroll_bottom()

off_campus_link = browser.find_elements_by_class_name('td-read-more')
print(len(off_campus_link),type(off_campus_link))

for a in range(len(off_campus_link)):
   
    cmp_link = off_campus_link[a].find_element_by_tag_name('a')
    if(cmp_link.get_attribute('href')):
        new = cmp_link.get_attribute('href')
        print("Link - ",new)
        total.append(new)
    else:
        continue


for l in range(len(total)):
    browser.get(total[l])
    scroll_bottom()
    apply_link = browser.find_element_by_xpath("//*[contains(text(), 'Apply Link')]")
    print(apply_link.text)
    apply_link = apply_link.find_element_by_tag_name('a')
    apply_link = apply_link.get_attribute('href')
    print('Fina Link - ',apply_link)
    

		
print("done!")



browser.close()