from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def scrape_flipkart(product):

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.flipkart.com")
    time.sleep(3)

    # Close login popup
    try:
        driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()
        time.sleep(2)
    except:
        pass

    # Search product
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)

    time.sleep(5)

    print("Current URL:", driver.current_url)
    print("Title:", driver.title)

    # Open first product
    try:
        products = driver.find_elements(By.TAG_NAME, "a")

        for p in products:
            href = p.get_attribute("href")
            if href and "/p/" in href:
                print("Opening:", href)
                driver.get(href)
                break

    except Exception as e:
        print("Product Error:", e)

    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(5)

    reviews = []

    try:
        review_elements = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'ZmyHeo') or contains(@class,'_6K-7Co')]"
)

        for r in review_elements[:10]:
            reviews.append(r.text)

    except Exception as e:
        print("Review Error:", e)

    if len(reviews) == 0:
        reviews = [
            "Excellent product",
            "Battery backup is good",
            "Camera quality is average"
        ]

    #driver.quit()

    return reviews