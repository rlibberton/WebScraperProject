from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from bs4 import BeautifulSoup
import pandas as pd
#import MySQLdb

#conn = MySQLdb.connect(host='localhost', user='root', passwd='')

print('Starting Driver') #For testing purposes only

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

counties = [] #List to store the name of the counties
active_power_outages = [] #List to store the active power outages
customers_without_power = [] #List to store number of customers without power
customers_served = []
driver.get('https://outagemaps.duke-energy.com/#/carolinas') #communicates with webdriver to open URL


python_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/carolinas-selection/section/div/div[2]/div[1]/a/span')))
python_button.click() #clicks the "Carolinas"

python_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/outage-home/section/user-onboarding/div/div/div/div/div[3]/button")))
python_button2.click()

python_button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/outage-home/section/maps-panel/div/section/button")))
python_button3.click()

python_button4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/outage-home/section/maps-panel/div/section[2]/div[3]/div[3]/button[2]")))
python_button4.click()

content = driver.page_source 
soup = BeautifulSoup(content, 'lxml')

#Prints all the counties in the outage summary
divs = soup.find_all('div', {'class': "county-panel-outage-info ng-tns-c0-0 ng-star-inserted"})
for div in divs:
    counties.append(div.contents[1].contents[1].text)
    active_power_outages.append(div.contents[3].contents[3].text)
    customers_without_power.append(div.contents[5].contents[3].text)
    customers_served.append(div.contents[7].contents[3].text) 
print(len(divs))
print(counties)  
print(active_power_outages)
print(customers_without_power)
print(customers_served)

print('Driver has ended')