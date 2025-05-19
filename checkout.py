import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from navigation import navigate_to_checkout

def process_checkout(driver):
    navigate_to_checkout(driver)
    
    driver.execute_script("window.scrollTo(0, 300)")
    account = driver.find_element(By.XPATH, "//input[@value='guest']")
    account.click()
    driver.find_element(By.ID, "button-account").click()
    time.sleep(1)
    
    fill_billing_details(driver)
    
    driver.find_element(By.ID, "button-guest").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "button-shipping-method").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@name='agree']").click()
    driver.find_element(By.ID, "button-payment-method").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "button-confirm").click()
    time.sleep(1)

def fill_billing_details(driver):
    first_name = driver.find_element(By.ID, "input-payment-firstname")
    first_name.click()
    first_name.send_keys("Mehedi")
    time.sleep(0.5)
    
    last_name = driver.find_element(By.ID, "input-payment-lastname")
    last_name.click()
    last_name.send_keys("Hasan")
    time.sleep(0.5)
    
    email = driver.find_element(By.ID, "input-payment-email")
    email.click()
    email.send_keys("hasan@gmail.com")
    time.sleep(0.5)
    
    telephone = driver.find_element(By.ID, "input-payment-telephone")
    telephone.click()
    telephone.send_keys("2093472348")
    time.sleep(0.5)
    
    address_1 = driver.find_element(By.ID, "input-payment-address-1")
    address_1.click()
    address_1.send_keys("Mohammadpur")
    time.sleep(0.5)
    
    city = driver.find_element(By.ID, "input-payment-city")
    city.click()
    city.send_keys("Dhaka")
    time.sleep(0.5)
    
    postcode = driver.find_element(By.ID, "input-payment-postcode")
    postcode.click()
    postcode.send_keys("1207")
    time.sleep(0.5)
    
    country = driver.find_element(By.ID, "input-payment-country")
    select_country = Select(country)
    select_country.select_by_value("18")
    time.sleep(0.5)
    
    region = driver.find_element(By.ID, "input-payment-zone")
    select_region = Select(region)
    select_region.select_by_visible_text("Dhaka")
    time.sleep(1)