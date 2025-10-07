from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Point to your chromedriver loaction
service = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)


#Open calculator website
driver.get("https://www.marshu.com/articles/calculate-addition-calculator-add-two-numbers.php")
print("Website opened successfully!")
time.sleep(3)

#Access form elements
num1 = driver.find_element(By.NAME ,"n01")
num2 = driver.find_element(By.NAME ,"n02")

#Pass keys to form element
num1.send_keys(2)
num2.send_keys(10)

time.sleep(2)

#Click the calculate button
cal_button = driver.find_element(By.XPATH, '//input[@value = "Find Addition"]')
cal_button.click()

time.sleep(4)
driver.quit()