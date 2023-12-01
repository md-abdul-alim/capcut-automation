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
import constant

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--window-size=800,900")

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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


driver.get(constant.LOGIN_URL)

# Load old session into the browser
loadCookies()
print("driver.current_url: ", driver.current_url)

def ok_button(xpath):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"{xpath}"))).click()
        time.sleep(2)
        print("ok button")
    except Exception as e:
         print("Ok button error: ", e)

def login(driver):
    try:
        print('Please Login the the website')

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "signUsername"))).send_keys(constant.LOGIN_EMAIL)

        wait = WebDriverWait(driver, 5)
        continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lv-btn-primary")))
        continue_button.click()
        time.sleep(5)
        #-------------
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))).send_keys(constant.LOGIN_PASSWORD)
        time.sleep(3)
        #-------------
        sign_in_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lv_sign_in_panel_wide-primary-button")))
        sign_in_button.click()
        time.sleep(15)

        # After successful login save new session cookies ot json file
        saveCookies(driver)
    except Exception as e:
        if 'cookies.json' in os.listdir():
            os.remove("cookies.json")
            login(driver)


if 'https://www.capcut.com/my-edit?enter_from=login' in driver.current_url:
    print('Previous session loaded')
else:
    login(driver)
    

driver.get(constant.DASHBOARD_URL)

skip_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.guide-modal-footer-btn.guide-modal-footer-skip-btn')))
skip_button.click()
time.sleep(2)

upload_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "cover-placeholder")))
upload_button.click()

#-------------
ok_button(constant.POPUP_XPATH)

#scroll down for filter
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "lv-tabs-down-icon"))).click()
print("scroll working.........")
time.sleep(5)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "side-tab-filter"))).click()
print("filter clicked.")
 
#-------------------------------
for i in range(1, 3):
    text_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, f"//*[text()='{constant.FILTER_NAME}']")))
    parent_element = text_element.find_element(By.XPATH, "..")
    parent_element.click()
    print("select filter")
    time.sleep(5)
    #----scroll horizontal filter-----
    element = driver.find_element(By.CLASS_NAME, "timeline-play-cursor-hd")
    ActionChains(driver).click_and_hold(element).move_by_offset(constant.HORIZONTAL_BAR_WIDTH, 0).release().perform()
    time.sleep(5)
#---------------------------------
time.sleep(1)
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/button"))).click()

ok_button(constant.POPUP_XPATH)

intensity_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, constant.BASIC_INTENSITY_XPATH)))
intensity_input.send_keys(Keys.CONTROL, 'a')
intensity_input.send_keys(constant.BASIC_INTENSITY_VALUE)
intensity_input.send_keys(Keys.RETURN)
time.sleep(2)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "segment-widget"))).click()
# //*[@id="canvas-cover"]/div

time.sleep(195)
# close the browser
driver.quit()

print('Finished ...')