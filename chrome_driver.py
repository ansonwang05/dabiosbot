from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--headless") # Invisible Chrome 
#chrome_options.add_argument("--disable-gpu") # For older Windows devices
chrome_options.add_argument("--log-level=3") # Suppresses most warnings

prefs = {
    "profile.managed_default_content_settings.images": 2, 
    "profile.managed_default_content_settings.stylesheets": 2,
    "profile.managed_default_content_settings.fonts": 2
}
chrome_options.add_experimental_option("prefs", prefs)

def create_driver():
    driver = webdriver.Chrome(options=chrome_options)

    driver.set_page_load_timeout(10)
    return driver 

def safe_get(driver, url, retries=3, wait_time=2):
    attempt = 0
    while attempt < retries:
        try: 
            driver.get(url)
            return True # Webpage Loaded 
        except (TimeoutError, Exception) as e: 
            print(f"Attempt {attempt + 1} Failed: {e}")
            attempt += 1
            time.sleep(wait_time)
    return False # Failed to get webpage