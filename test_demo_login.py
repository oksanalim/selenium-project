from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_demo_login():
    # Start Firefox browser
    driver = webdriver.Firefox()

    # Go to login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Enter username
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    # Enter password
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Click login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait and assert success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        assert "You logged into a secure area!" in success_message.text
        print("✅ Login successful!")
    except Exception as e:
        print("❌ Login failed!")
        raise e
    finally:
        driver.quit()

if __name__ == "__main__":
    test_demo_login()
