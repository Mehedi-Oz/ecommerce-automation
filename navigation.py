import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def navigate_to_homepage(driver):
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(1)

def navigate_to_phones(driver):
    phones = driver.find_element(By.XPATH, "//a[text()='Phones & PDAs']")
    phones.click()
    time.sleep(1)

def navigate_to_laptops(driver):
    laptop_and_notebooks = driver.find_element(
        By.XPATH, "//a[text()='Laptops & Notebooks']"
    )
    time.sleep(1)

    action = ActionChains(driver)
    action.move_to_element(laptop_and_notebooks).perform()
    driver.find_element(
        By.XPATH, "//a[normalize-space()='Show AllLaptops & Notebooks']"
    ).click()
    time.sleep(1)

def navigate_to_cart(driver):
    cart_total = driver.find_element(By.ID, "cart-total")
    cart_total.click()
    time.sleep(1)
    
    view_cart = driver.find_element(By.XPATH, "//strong[normalize-space()='View Cart']")
    view_cart.click()
    time.sleep(1)

def navigate_to_checkout(driver):
    checkout = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    checkout.click()
    time.sleep(1)