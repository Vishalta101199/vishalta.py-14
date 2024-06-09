from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Configuration ---
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

# --- Setup ---
driver = webdriver.Chrome()  # Or another browser driver
driver.get(url)

# --- Cookies Before Login ---
cookies_before = driver.get_cookies()
print("----- Cookies Before Login -----")
for cookie in cookies_before:
    print(cookie)

# --- Login ---
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

# Wait for the dashboard to load
WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))

# --- Cookies After Login ---
cookies_after = driver.get_cookies()
print("\n----- Cookies After Login -----")
for cookie in cookies_after:
    print(cookie)

# --- Verification (Check if New Cookies) ---
new_cookies = [c for c in cookies_after if c not in cookies_before]
if new_cookies:
    print("\n----- New Cookies Generated During Login -----")
    for cookie in new_cookies:
        print(cookie)

# --- Logout ---
driver.find_element(By.ID, "react-burger-menu-btn").click()  # Open menu
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
).click()

# --- Close Browser ---
driver.quit()