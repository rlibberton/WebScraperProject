from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
#import MySQLdb

#conn = MySQLdb.connect(host='localhost', user='root', passwd='')

print('Starting Driver') #For testing purposes only

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

counties = [] #List to store the name of the counties
active_power_outages = [] #List to store the active power outages
customers_without_power = [] #List to store number of customers without power
driver.get('https://outagemaps.duke-energy.com/#/carolinas') #communicates with webdriver to open URL

driver.implicitly_wait(10)
python_button= driver.find_element_by_css_selector('.jurisdiction-selection-select-state:nth-child(4) > .jurisdiction-selection-select-state__item:nth-child(1) .jurisdiction-selection-select-state__item-text').click() #clicks the "Carolinas "


driver.implicitly_wait(10)
#soup = BeautifulSoup(content, 'lxml')

#while True:
 #   driver.implicitly_wait(5)
 #   spans = soup.find_all('span', {'class': 'county-panel-outage-info-heading-text'}) # or span by class name
 #   if spans:
 #       break
driver.implicitly_wait(10)
button2 = driver.find_element_by_xpath("/html/body/app-root/outage-home/section/user-onboarding/div/div/div/div/div[3]/button").click()
driver.implicitly_wait(10)
button3 = driver.find_element_by_xpath("/html/body/app-root/outage-home/section/maps-panel/div/section/button").click()
driver.implicitly_wait(10)
button4 = driver.find_element_by_xpath("/html/body/app-root/outage-home/section/maps-panel/div/section[2]/div[3]/div[3]/button[2]").click()
driver.implicitly_wait(10)

content = driver.page_source 
soup = BeautifulSoup(content, 'lxml')
driver.implicitly_wait(10)
spans = soup.find_all('span', {'class': "county-panel-outage-info-heading-text"}) # or span by class name
for span in spans:
    print(span.text)

print('Driver has ended')