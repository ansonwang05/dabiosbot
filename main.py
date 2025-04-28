import chrome_driver as cd

url = "https://leetcode.com/problemset/"

driver = cd.create_driver()

if cd.safe_get(driver, url):
    print(driver.title)
else:
    print("Failed to load page") 