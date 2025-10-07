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
    time.sleep(3)
    
    #Different ways to find elements
    print("Finding elements using different methods")
    
    #By ID
    try:
        element = driver.find_element(By.ID, "user-name")
        print("✓ Found by ID")
    except:
        print("✗ Not found by ID")
            
    #By NAME
    try:
        element = driver.find_element(By.NAME, "user-name")
        print("✓ Found by NAME")
        
    except:    
        print("✗ Not found by NAME")
        
    #By CLASS_NAME
    try:
        element = driver.find_element(By.CLASS_NAME, "login_logo")
        print("✓ Found by CLASS_NAME")
        
    except:    
        print("✗ Not found by CLASS_NAME")
        
    #By CSS_SELECTOR
    try:
        element = driver.find_element(By.CSS_SELECTOR, "#user-name")
        print("✓ Found by CSS_SELECTOR")
        
    except:    
        print("✗ Not found by CSS_SELECTOR")
        
    #By XPATH
    try:
        element = driver.find_element(By.XPATH, "//input[@placeholder = 'Password']")
        print("✓ Found by XPATH")
        
    except:    
        print("✗ Not found by XPATH")
    

except Exception as e:
    print(f" x Error: {e}")
    
finally: 
    time.sleep(4)   
    driver.quit()