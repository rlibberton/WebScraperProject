from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
#import MySQLdb

#conn = MySQLdb.connect(host='localhost', user='root', passwd='')


driver = webdriver.Chrome("/usr/local/bin/chromedriver")

counties = [] #List to store the name of the counties
active_power_outages = [] #List to store the active power outages
customers_without_power = [] #List to store number of customers without power
driver.get('https://outagemaps.duke-energy.com/#/carolinas') #communicates with webdriver to open URL

driver.implicitly_wait(10)
python_button= driver.find_element_by_css_selector('.jurisdiction-selection-select-state:nth-child(4) > .jurisdiction-selection-select-state__item:nth-child(1) .jurisdiction-selection-select-state__item-text').click() #clicks the "Carolinas "

driver.implicitly_wait(10)
content = driver.page_source 
soup = BeautifulSoup(content, 'lxml')
#for a in soup.find_all("div", class_ = "county-panel-outage-info-heading"):
#    county = a.get('span', class_= 'county-panel-outage-info-heading-text')
#    counties.append(county.text)

counties = soup.find_all('span', attrs={'class': 'county-panel-outage-info-heading-text'})
print(counties)
#name = county_holder.text.strip()


#print(name)