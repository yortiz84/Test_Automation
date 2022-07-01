from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert

s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('http://www.uitestingplayground.com/')

Class_At_butt=driver.find_element(By.PARTIAL_LINK_TEXT, 'Verify Text')
Class_At_butt.click()

text=driver.find_element(By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")
