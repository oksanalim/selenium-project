{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "643fbf4c-450b-4471-860a-7f19e031c846",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ℹ️ No cookie banner shown\n",
      "🔎 Found 9 results\n",
      "🔹 Selenium Python Tutorial (with Example)\n",
      "🔹 Selenium With Python Tutorial & Examples\n",
      "🔹 Selenium Python Tutorial\n",
      "🔹 Selenium 4.7 Automation with Python: A Comprehensive ...\n",
      "🔹 Selenium with Python — Selenium Python Bindings 2 ...\n",
      "🔹 UI Automation using Python and Selenium: Tutorial\n",
      "🔹 Selenium Webdriver with PYTHON from Scratch + ...\n",
      "🔹 Selenium Python Full Course 2025 | Master Web Automation ...\n",
      "🔹 Selenium Python Tutorial: Guide With Examples\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.firefox.service import Service as FirefoxService\n",
    "from selenium.webdriver.firefox.options import Options\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "import time\n",
    "\n",
    "def test_google_search():\n",
    "    # Optional: Run Firefox in headless mode\n",
    "    # options = Options()\n",
    "    # options.headless = True\n",
    "\n",
    "    # Initialize Firefox WebDriver\n",
    "    driver = webdriver.Firefox()  # Add 'options=options' if headless\n",
    "\n",
    "    driver.get(\"https://www.google.com\")\n",
    "\n",
    "    # Handle cookie consent if present\n",
    "    try:\n",
    "        consent_button = WebDriverWait(driver, 5).until(\n",
    "            EC.element_to_be_clickable((By.XPATH, \"//div[contains(text(), 'Accept all') or contains(text(), 'I agree')]\"))\n",
    "        )\n",
    "        consent_button.click()\n",
    "        print(\"✅ Accepted cookies\")\n",
    "        time.sleep(1)\n",
    "    except:\n",
    "        print(\"ℹ️ No cookie banner shown\")\n",
    "\n",
    "    # Search for something\n",
    "    search_box = driver.find_element(By.NAME, \"q\")\n",
    "    search_box.send_keys(\"Selenium testing with Python\")\n",
    "    search_box.send_keys(Keys.RETURN)\n",
    "\n",
    "    # Wait for results to load\n",
    "    WebDriverWait(driver, 10).until(\n",
    "        EC.presence_of_element_located((By.CSS_SELECTOR, \"h3\"))\n",
    "    )\n",
    "\n",
    "    results = driver.find_elements(By.CSS_SELECTOR, \"h3\")\n",
    "    print(f\"🔎 Found {len(results)} results\")\n",
    "\n",
    "    for r in results:\n",
    "        print(\"🔹\", r.text)\n",
    "\n",
    "    assert len(results) > 0, \"❌ No search results found!\"\n",
    "\n",
    "    driver.quit()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    test_google_search()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0ed5e15-63a6-495e-9792-dad342aadc5c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
