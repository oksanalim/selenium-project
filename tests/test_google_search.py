from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium testing")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Simple wait for demo purposes

    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0, "No search results found!"

    print("✅ First search result:", results[0].text)
    
    driver.quit()

if __name__ == "__main__":
    test_google_search()
