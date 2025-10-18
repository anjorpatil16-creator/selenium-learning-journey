'''
Author: Anjor Patil
Date : 11-10-2025
Time: 12:11

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Open browser in incogniti mode(To avoid google manager's popup)
chrome_option = Options()
chrome_option.add_argument("--incognito")

#Give webdriver path
driver_path = Service(r"C:/chromedriver/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=driver_path, options= chrome_option)
wait = WebDriverWait(driver, 10)


try:
    
    #Login
    driver.get("https://www.saucedemo.com")
    print("Website opened")
    
    #Enter username and password
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("visual_user")
    print("Username entered")
    
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    print("Password entered")
    
    #Click on login button
    login_btn = driver.find_element(By.ID ,"login-button")
    login_btn.click()
    print("Logged in")
    time.sleep(3)
    
    #Wait for products page
    # dropdown_btn = driver.find_element(By.CLASS_NAME, "product_sort_container")
    # dropdown_btn.click()
    # time.sleep(3)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    
    #Find dropdown
    dropdown_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown = Select(dropdown_element)
    
    print("Found dropdown")
    print(type(dropdown))
    
    #Print all options
    print("\nAvailable sorting options:")
    for opt in dropdown.options:
        print(f" -{opt.text}")
        
    
    #Test 1: Sort by Name(Z to A)
    print("\n--- Test 1: Sort Z to A ---")
    dropdown.select_by_visible_text("Name (Z to A)")   
    time.sleep(3)
    
    #Get first product name
    first_prod = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(f" First product after Z-A sort: {first_prod}")
    
    # Test 2: Sort by Price (low to high)
    print("\n--- Test 2: Sort Price Low to High ---")
    dropdown_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown = Select(dropdown_element)  
    dropdown.select_by_value("lohi")
    time.sleep(2)
    
    # Wait for the first product to be reloaded/refreshed
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_price")))

    
    #Print first product name and price
    first_product = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    first_prod_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n First Product: {first_product} - {first_prod_price}")    
    
    # Test 3: Sort by Price (high to low)
    dropdown_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown = Select(dropdown_element)
    print("\n--- Test 3: Sort Price High to Low ---")
    dropdown.select_by_value("hilo")
    time.sleep(2)
    
    #Print first product name and price
    first_product = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    first_prod_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n First Product: {first_product} - {first_prod_price}")    
    
    
    # dropdown_option = driver.find_element(By.XPATH, "//option[@value = 'lohi']")
    # dropdown_option.click()
    time.sleep(10)
    
    
except Exception as e:
    print(f" Error: {e}")
    
finally:
    driver.quit()
    print("✓ Dropdown test completed")        