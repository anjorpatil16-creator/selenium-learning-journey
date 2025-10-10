"""
Author: Anjor Patil
Date: 04-10-2025
Time: 17:00
Environment: VS Code and Git Bash
Goal: Automate Google Search and navigate DeepseekAI website using Selenium

Description:
This script opens a Chrome browser, navigates to Google, then visits the DeepseekAI website,
clicks on the chat start button, waits for the page to load, and finally closes the browser.

Prerequisites:
- Selenium installed (pip install selenium)
- Compatible ChromeDriver downloaded and path correctly set

"""



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