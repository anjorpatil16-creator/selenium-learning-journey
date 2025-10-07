#Created and owned by Anjor Patil on 05-10-2025 at 21.41
#Goal: Automate login on demo website

#Import required modules and libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Setup
service = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    #Open browser with given website URL
    driver.get("https://www.saucedemo.com")
    print("Website opened successfully")
    time.sleep(5)
    
    #Find username field and enter username
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    print("Username entered")
    time.sleep(2)
    
    #Find password field and enter password
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    print("Password entered")
    time.sleep(2)
    
    
    #Click on login button
    login_button = driver.find_element(By.XPATH, '//input[@type="submit" and @id= "login-button"]')
    login_button.click()
    print("Clicked Login!")
    time.sleep(6)
    
    #Check if we're on products page
    if  "inventory.html" in driver.current_url:
        print("✓ Login successful!")
    
    else:
        print("✗ Login failed!")
        
    print("Test run successfully!")
    
    

except Exception as e:
    print(f" x Error: {e}")
    
finally:    
    driver.quit()