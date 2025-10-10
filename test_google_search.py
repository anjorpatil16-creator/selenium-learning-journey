# Author: Anjor Patil
# Date: 05-10-2025
# Time: 20:00
# Environment: VS Code and Git Bash
# Goal: Automate Google Search



"""
This script automates a Google search using Python.

It opens a web browser, navigates to Google's homepage,
enters a specified search query, and retrieves or displays
the search results automatically.

Modules used:
- selenium: for browser automation
- time: for handling delays

"""



#Import required modules and libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Setup #Point to your chromedriver location
service = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe") #ChromeDriver path
driver = webdriver.Chrome(service=service)

try:
    #Open Google
    driver.get("https://www.google.com")
    print("Google Opened Successfully!")

    #Wait for 3 seconds
    time.sleep(3)

    #Get searchbox
    search_box = driver.find_element(By.NAME , "q")
    print("Found the searchbox!")

    #Type search query
    search_box.send_keys("Enola Holmes 3")
    time.sleep(8)

    #Press enter
    search_box.send_keys(Keys.ENTER)

    #Wait to see results
    time.sleep(30)
    print("Searched query on google successfully!")

except Exception as e:
    print(f"x Error : {e}")
    
    
finally:    
    driver.quit()
    print("Test completed! Well Done!")