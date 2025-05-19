from selenium import webdriver

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver