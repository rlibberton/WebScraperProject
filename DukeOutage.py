from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
import pymysql.cursors


def removeComma(poorlyFormatedString):
    output = ""
    for c in poorlyFormatedString:
        if c != ',':
            output = output + c
    return output

#Login info
#
#
#
#
#

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

counties = [] #List to store the name of the counties
active_power_outages = [] #List to store the active power outages
customers_without_power = [] #List to store number of customers without power
customers_served = []
current_time = []
driver.get('https://outagemaps.duke-energy.com/#/carolinas') #communicates with webdriver to open URL

try:
    python_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/carolinas-selection/section/div/div[2]/div[1]/a/span')))
    python_button.click() #clicks the "Carolinas"
except TimeoutException:
    pass
except NoSuchElementException:
    pass

try:
    python_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/outage-home/section/user-onboarding/div/div/div/div/div[3]/button")))
    python_button2.click()
except TimeoutException:
    pass
except NoSuchElementException:
    pass

try:
    python_button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/outage-home/section/maps-panel/div/section/button")))
    python_button3.click()
except TimeoutException:
    pass
except NoSuchElementException:
    pass

try:
    python_button4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/outage-home/section/maps-panel/div/section[2]/div[3]/div[3]/button[2]")))
    python_button4.click()
except TimeoutException:
    pass
except NoSuchElementException:
    pass

content = driver.page_source 
soup = BeautifulSoup(content, 'lxml')



divs = soup.find_all('div', {'class': "county-panel-outage-info ng-tns-c0-0 ng-star-inserted"})
for div in divs:
    counties.append(div.contents[1].contents[1].text)
    active_power_outages.append(int(removeComma(div.contents[3].contents[3].text)))
    customers_without_power.append(int(removeComma(div.contents[5].contents[3].text)))
    customers_served.append(int(removeComma(div.contents[7].contents[3].text)))

now = datetime.now()

current_time.append(now.strftime("%m/%d/%Y, %H:%M:%S"))

countiesMap = {}
neededToAddCounties = []
tester = True
try:
   with connection.cursor() as cursor:
        sql = "SELECT * FROM counties"
        cursor.execute(sql)
        results = cursor.fetchall()
        for county in results:
            id = county['id']
            name = county['name']
            countiesMap[name] = id
        for county in counties:
            notFound = True
            for mappedCounty in countiesMap.keys():
                if(mappedCounty == county):
                    notFound=False
                    break
            if notFound:
                neededToAddCounties.append(county)
        for county in neededToAddCounties:
            insertCountySql = "INSERT INTO counties (name) VALUES('{}')".format(county)
            cursor.execute(insertCountySql)
        connection.commit()
        tester= False
finally:
    if tester:
        connection.close()

try:
   with connection.cursor() as cursor:
        sql = "SELECT * FROM counties"
        cursor.execute(sql)
        results = cursor.fetchall()
        for county in results:
            id = county['id']
            name = county['name']
            countiesMap[name] = id

        thisCountyId=0
        thisCustomersServed = 0
        thisCustomersWithoutPower = 0

        for i in range(len(counties)):
            thisCountyId = countiesMap[counties[i]]
            thisCustomersServed = customers_served[i]
            thisCustomersWithoutPower = customers_without_power[i]
            sql = "INSERT INTO `records` (countyId, customersWithoutPower, customersServed, time) VALUES ({},{},{},'{}')".format(thisCountyId,thisCustomersWithoutPower,thisCustomersServed,now)
            cursor.execute(sql)
        connection.commit()

finally:
    connection.close()

driver.quit()
