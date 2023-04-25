import time
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


DRIVER_PATH = 'chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://clickspeedtest.com/")
button = driver.find_element(By.ID, "clicker")
counter = 0
while counter < 100:
    button.click()
    counter = counter + 1

input("Enter anything to close: ")


