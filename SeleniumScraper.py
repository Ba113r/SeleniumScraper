from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

# DRIVER_PATH = 'chromedriver.exe'
# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get("https://www.nintendo.com/")
# # print(driver.page_source)
# # driver.quit()

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.google.com/")