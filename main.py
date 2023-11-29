# selenium 4
import os
from selenium import webdriver
import json
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

email="alim.abdul.5915@gmail.com"
password="adminmilon"


def saveCookies(driver):
    cookies = driver.get_cookies()

    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print('New Cookies saved successfully')


def loadCookies():
    # Check if cookies file exists
    if 'cookies.json' in os.listdir():

        with open('cookies.json', 'r') as file:
            cookies = json.load(file)

        for cookie in cookies:
            driver.add_cookie(cookie)
    else:
        print('No cookies file found')
    
    driver.refresh() # Refresh Browser after login


loginURL = 'https://www.capcut.com/login'
driver.get(loginURL)

# Load old session into the browser
loadCookies()

if 'my-edit?enter_from=login' not in driver.current_url:
    print('Please Login the the website')
    # print('Press Enter after successful login ...')
    # input('>: ')
    try:
    	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "signUsername"))).send_keys(email)
    except Exception as e:
    	print(e)

    wait = WebDriverWait(driver, 5)
    continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lv-btn-primary")))
    continue_button.click()
    time.sleep(5)
    #-------------
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
    time.sleep(3)
    #-------------
    sign_in_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lv_sign_in_panel_wide-primary-button")))
    sign_in_button.click()
    time.sleep(15)

    # After successful login save new session cookies ot json file
    saveCookies(driver)

else:
    print('Previous session loaded')
    

driver.get("https://www.capcut.com/editor?enter_from=create_new&from_page=work_space&__action_from=my_draft&position=my_draft&scenario=tiktok_ads&scale=9%3A16")

wait = WebDriverWait(driver, 3)
skip_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.guide-modal-footer-btn.guide-modal-footer-skip-btn')))
skip_button.click()
time.sleep(2)

wait = WebDriverWait(driver, 2)
upload_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "icon-upload-wrap")))
upload_button.click()
time.sleep(10)
#-------------
try:
	wait = WebDriverWait(driver, 5)
	ok_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/div[4]/div/button")))
	ok_button.click()
	time.sleep(5)
	print("ok button")
except Exception as e:
	print(e)


# close the browser
driver.quit()


print('Finished ...')