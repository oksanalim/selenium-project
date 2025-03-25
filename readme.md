#  Selenium Testing with Python & Firefox (GeckoDriver)

This repository contains automated browser UI tests using **Selenium**, written in **Python**, and executed in **Firefox** with **GeckoDriver**.

---

##  Current Test(s)

###  Google Search Test
Performs a Google search and verifies that search results are displayed.

**Steps Automated:**
1. Open `https://www.google.com`
2. Handle cookie consent (if shown)
3. Type "Selenium testing with Python" into the search bar
4. Assert that results (h3 tags) appear on the page

###  Login Form Test
Tests a public login form at [the-internet.herokuapp.com](https://the-internet.herokuapp.com/login).

**Steps Automated:**
1. Open login page
2. Enter valid credentials (`tomsmith` / `SuperSecretPassword!`)
3. Click login
4. Assert success message appears

---

## Project Structure

```
selenium-firefox-tests/
├── tests/
│   ├── test_google_search.py
│   └── test_demo_login.py
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

### 3. Run the Tests
```bash
python tests/test_google_search.py
python tests/test_demo_login.py
```

---

## Tech Stack
- Python 3
- Selenium WebDriver
- Firefox + GeckoDriver

---

##  Roadmap
- [x] Google search test
- [x] Login form test
- [ ] Automate failed login scenario
- [ ] Add PyTest test runner
- [ ] Add GitHub Actions for CI
- [ ] Add headless test mode



Happy testing! 

## Author
[Oksana Lim](https://github.com/oksanalim)

---

Happy testing! 

