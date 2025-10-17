'''
Author: Anjor Patil
Date : 07-10-2025
Time: 21:25

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driverpath = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service= driverpath)

try:
    
    driver.get("https://www.saucedemo.com")
    print("Website saucedemo opened!")
     
    wait = WebDriverWait(driver, 10)
    
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    print("Username entered")
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    print("Password entered")
    
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    print("Login button clicked")
    
    #Wait specifically for title to be visible
    title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    print(f"Page loaded: {title.text}")
    
    
    items = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    print(f"Found {len(items)} products")
    
    for i in items:
        print(i.text)
        
except Exception as e:
    print(f"Error: {e}")
    
finally:
    driver.quit()
    print("Test completed!")        
