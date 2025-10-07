from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


#Point to your chromedriver loaction
service = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Open Google
driver.get("https://www.google.com")
print("Browser opened successfully!")

#Wait 3 seconds
time.sleep(3)


#Open deepseekAI website
driver.get("https://www.deepseek.com")
time.sleep(2)
start_button = driver.find_element(By.XPATH , '//a[@href="https://chat.deepseek.com"]')
start_button.click()
time.sleep(5)


#Close browser
driver.quit()
print(" Test completed!")