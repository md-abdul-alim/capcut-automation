import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(2)
driver.find_element(By.ID, 'downloadButton').click()

time.sleep(5)

driver.quit()