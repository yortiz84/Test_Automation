from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert

s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('http://www.uitestingplayground.com/')

Class_At_butt=driver.find_element(By.PARTIAL_LINK_TEXT, 'Class Attribute')
Class_At_butt.click()

#positive test
boton1=driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '),' btn-primary ')]")
boton1.click()

a = driver.switch_to.alert
a.accept()

#negative test
boton2=driver.find_element(By.XPATH, "//button[@class='btn-primary']")
boton2.click()

boton1.click()
#driver.close()
