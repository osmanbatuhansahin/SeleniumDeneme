import random

from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Firefox()

url = "https://yokatlas.yok.gov.tr/lisans.php?y=100711046"


from selenium.webdriver.common.action_chains import ActionChains

# button = driver.find_element_by_id("headingOne")
# print(button.text)
# driver.implicitly_wait(1)
# ActionChains(driver).move_to_element(button).click(button).perform()
#
# elements = driver.find_elements_by_css_selector('.table table-bordered')
# print(elements)
# for element in elements:
#     print(element.text)
#
driver.get(url)

sol=[]
sag=[]


for i in list(range(2,14)):
   myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div["+str(i)+"]/div")
   myBtn.click()

   #print(myBtn.text)
time.sleep(2)
elementsRight = driver.find_elements_by_css_selector('.vert-align')
for elementRight in elementsRight:
   sag.append(elementRight.text)

elementsLeft = driver.find_elements_by_css_selector('.text-left')
for elementLeft in elementsLeft:
   sol.append(elementLeft.text)

dictionary = dict(zip(sol, sag))

print ( dictionary)
#
# for element in elements:
#     print(element.text)
# elements = browser.find_elements_by_css_selector('.table table-bordered')
# time.sleep(2)
#
# for element in elements:
#     print(element.text)