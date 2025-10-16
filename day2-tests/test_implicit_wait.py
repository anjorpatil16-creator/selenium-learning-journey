'''
Author: Anjor Patil
Date : 06-10-2025
Time: 14:21

'''



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driverpath = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=driverpath)

driver.implicitly_wait(10)

try:
    #Open website
    driver.get("https://www.saucedemo.com")
    print("Saucedemo opened!")
    
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("visual_user")
    print("Username field accessed and key passed")
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    print("Password field accessed and key passed")
    
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    print("Login button clicked!")
    
    product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    print(f"Products: {product.text}")
    
    time.sleep(3)
        
except Exception as e:
       print(f"Error: {e}")
       
finally:
    driver.quit()
    print("Test completed!")   