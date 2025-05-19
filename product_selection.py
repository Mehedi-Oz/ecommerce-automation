import os
import time
import random
from selenium.webdriver.common.by import By
from navigation import navigate_to_phones, navigate_to_laptops, navigate_to_cart

def browse_phones(driver):
    navigate_to_phones(driver)
    
    iphone = driver.find_element(By.XPATH, "//a[text()='iPhone']")
    iphone.click()
    time.sleep(1)
    
    clicking_iphone_img = driver.find_element(By.XPATH, "//ul[@class='thumbnails']//li[1]")
    clicking_iphone_img.click()
    time.sleep(1)
    
    for i in range(0, 5):
        next_image = driver.find_element(
            By.XPATH, "//button[@title='Next (Right arrow key)']"
        )
        next_image.click()
        time.sleep(1)
        
        if i == 2:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            screenshot_path = os.path.join(
                "screenshots", f"screenshot_{random.randint(0, 1001)}.png"
            )
            driver.save_screenshot(screenshot_path)

    driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()
    time.sleep(2)
    
    quantity_iphone = driver.find_element(By.ID, "input-quantity")
    quantity_iphone.clear()
    quantity_iphone.send_keys(2)
    adding_iphone_to_cart = driver.find_element(By.ID, "button-cart")
    adding_iphone_to_cart.click()
    time.sleep(1)

def browse_laptops(driver):
    navigate_to_laptops(driver)
    
    driver.execute_script("window.scrollTo(0, 300)")
    time.sleep(1)
    hp_laptop = driver.find_element(By.XPATH, "//a[text()='HP LP3065']")
    hp_laptop.click()
    time.sleep(1)
    
    driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(1)
    
    calender_icon = driver.find_element(By.XPATH, "//i[@class='fa fa-calendar']")
    calender_icon.click()
    
    click_next_to_calender = driver.find_element(By.XPATH, "//th[@class='next']")
    delivery_month_year = "May 2012"
    
    while True:
        month_year = driver.find_element(By.XPATH, "//th[@class='picker-switch']").text
        if month_year == delivery_month_year:
            break
        click_next_to_calender.click()
    
    delivery_date = driver.find_element(By.XPATH, "//td[text()='30']")
    delivery_date.click()
    time.sleep(1)
    
    adding_laptop_to_cart = driver.find_element(By.ID, "button-cart")
    adding_laptop_to_cart.click()
    time.sleep(1)
    
    navigate_to_cart(driver)
    
    canceling_iphone_order = driver.find_element(By.XPATH, "//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]/i[1]")
    canceling_iphone_order.click()
    time.sleep(1)