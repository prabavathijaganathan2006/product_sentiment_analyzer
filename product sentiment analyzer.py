from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(3)

# Search product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("iPhone 16")
search_box.send_keys(Keys.ENTER)

time.sleep(5)

# Open first product
products = driver.find_elements(By.CSS_SELECTOR, "h2 a")

if len(products) > 0:
    products[0].click()
    time.sleep(5)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    # Get reviews
    reviews = driver.find_elements(By.CSS_SELECTOR, "span[data-hook='review-body']")

    print("Reviews:\n")

    if len(reviews) == 0:
        print("No reviews found")
    else:
        for i, review in enumerate(reviews, start=1):
            print(f"{i}. {review.text}")
            print("-" * 50)

else:
    print("No product found")

input("Press Enter to close...")
driver.quit()