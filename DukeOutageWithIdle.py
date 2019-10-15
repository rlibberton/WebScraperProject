from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

counties = [] #List to store the name of the counties
active_power_outages = [] #List to store the active power outages
customers_without_power = [] #List to store number of customers without power
driver.get('https://outagemaps.duke-energy.com/#/current-outages/ncsc') #communicates with webdriver to open URL

python_button= driver.find_element_by_css_selector('.jurisdiction-selection-select-state:nth-child(4) > .jurisdiction-selection-select-state__item:nth-child(1) .jurisdiction-selection-select-state__item-text').click() #clicks the "Carolinas "

content = driver.page_source 
soup = BeautifulSoup(content, features="lxml")
for a in soup.findAll('a', href=True, attrs={'class': 'county-panel-outage-info ng-tns-c0-0 ng-star-inserted'}):
    county = a.find('div', attrs={'county-panel-outage-info-heading-text'})
    counties.ap
    append(county.text)

print(counties)
exit()
