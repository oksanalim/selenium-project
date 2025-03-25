#  Selenium Testing with Python & Firefox (GeckoDriver)

This repository contains automated browser UI tests using **Selenium**, written in **Python**, and executed in **Firefox** with **GeckoDriver**.

---

##  urrent Test(s)

###  Google Search Test
Performs a Google search and verifies that search results are displayed.

**Steps Automated:**
1. Open `https://www.google.com`
2. Handle cookie consent (if shown)
3. Type "Selenium testing with Python" into the search bar
4. Assert that results (h3 tags) appear on the page

---

##  Project Structure

```
selenium-firefox-tests/
├── tests/
│   └── test_google_search.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install GeckoDriver (Firefox WebDriver)
- [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- Add it to your system `PATH`
- Confirm it's working:
```bash
geckodriver --version
```

### 3. Run the Test
```bash
python tests/test_google_search.py
```

---

## Tech Stack
- Python 3
- Selenium WebDriver
- Firefox + GeckoDriver

---

## Roadmap
- [x] Google search test
- [ ] Automate form/login example
- [ ] Add PyTest test runner
- [ ] Add GitHub Actions for CI
- [ ] Add headless test mode

---

## Author
[Your Name](https://github.com/oksanalim)

---

Happy testing! 

