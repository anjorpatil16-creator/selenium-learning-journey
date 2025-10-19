'''
Author: Anjor Patil
Date : 08-10-2025
Time: 11:15

'''



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
import time


#configure Chrome to disable password manager and related popups
chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--disable-save-password-bubble")

# chrome_options.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.notifications": 2,
#     "credentials_enable_service": False,
#     "profile.password_manager_enabled": False
# })


driverpath = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = driverpath, options=chrome_options)
wait = WebDriverWait(driver, 10)



try:
    
    driver.get("https://www.saucedemo.com")
    print("Website opened")
    
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    print("Username entered")
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    print("Password entered")
    
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    print("Login successful")
    
    backpack = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    print("Products page loaded")
    
    add_prod1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_prod1.click()
    print("Product 1 added")
    time.sleep(2)
    
  
    add_prod2 = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-fleece-jacket")))
    add_prod2.click()
    print("Product 2 added")
    time.sleep(3)
    
  
    #Verify cart badge shows total number of added products
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    
    if int(cart_badge) == 2:
        print(f"✓ Pass: Cart shows {cart_badge} items.")
    
    else:
        print(f"✗ FAIL: Expected 2 items but cart shows {cart_badge}")    
    
  
    #shopping cart
    cart_link = driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']")
    cart_link.click()
    print("Opened cart")
    time.sleep(4)
    
    #Verify items
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    print(f"Cart contains: {len(cart_items)} items")
    
    
    #Get item names
    print("Products are:")
    for i,item in enumerate(cart_items):
        item_names = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(i+1,item_names)
        
    

except Exception as e:
    print(f"Error: {e}")
    driver.save_screenshot("Day2-tests/error_screenshot.png")
    print("Screenshot saved")

finally:
    driver.quit()
    print("Test completed!")