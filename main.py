import os
from browser import setup_driver
from navigation import navigate_to_homepage
from product_selection import browse_phones, browse_laptops
from checkout import process_checkout


if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Setup browser
driver = setup_driver()

# Navigate to homepage
navigate_to_homepage(driver)

# Browse and add products
browse_phones(driver)
browse_laptops(driver)

# Process checkout
process_checkout(driver)

print("Order Confirmed!")

driver.close()
