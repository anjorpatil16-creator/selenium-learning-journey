'''
Author: Anjor Patil
Date : 20-10-2025
Time: 22:17

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time



#Open browser in incognito mode(Avoid popup)
chrome_option = Options()
chrome_option.add_argument("--incognito")

#Set webdriver path
driver_path = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=driver_path, options = chrome_option)
wait = WebDriverWait(driver, 30)

try:
    
    print("=======STARTING CHECKOUT TEST=======")
    
    
    #Step 1: Login
    print("STEP 1: Login")
    driver.get("https://www.saucedemo.com")
    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    print("Logged in\n")
    
    
    #STEP 2: Add products to cart
    print("STEP 2: Add products to cart")
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    
    #Add backpack
    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()
    print("Backpack added to cart")
    
    #Add T-shirt
    tshirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    tshirt.click()
    print("T-shirt added to cart\n")
    
    #STEP 3: Go to cart
    print("STEP 3: Open cart")
    cart_btn = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_btn.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    print("Cart opened\n")
    
    
    #STEP 4: Proceed to checkout
    print("STEP 4: Proceed to checkout")
    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()
    wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    print("On checkout page\n")
    
    
    #STEP 5: Fill checkout information
    print("STEP 5: Fill checkout info")
    
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Anjor")
    
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Patil")
    
    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("415698")
    
    #STEP 6: Continue
    print("STEP 6: Continue")
    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))
    print("On checkout overview page\n")
    
    #STEP 7: Verify items and total
    print("STEP 7: Verify order summary")
    total_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    print(f"Order contains: {len(total_items)} items")
    
    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    print(f"Price total: {total_price}\n")
    
    time.sleep(3)
    
    #STEP 8: Finish order
    print("STEP 8: Complete Order")
    finish = driver.find_element(By.ID, "finish")
    finish.click()
    
    #STEP 9: Verify success
    print("STEP 9: Verify Success")
    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    header_text = header.text
    
    if "Thank you for your order" in header_text:
        print(f"  Success! {header_text}")
    else:
        print(f" FAIL: Unexpected message: {header_text}")   
        
        
    print("\n=======CHECKOUT TEST COMPLETED SUCCESSFULLY=======")     
    time.sleep(3)
    
    
except Exception as e: 
    print(f"Error: {e}")
    driver.save_screenshot("Day2-tests/checkout_error.png")
    print("Screenshot saved.")
    
finally:  
    
    #Quit the chrome driver
    driver.quit()
    
    