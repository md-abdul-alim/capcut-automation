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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1200,800")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def text_to_seconds(time_text):
    # Use regular expression to extract hours, minutes, seconds, and milliseconds
    splitted_time = time_text.split(':')

    if len(splitted_time) == 3:
        minutes, seconds, milliseconds = map(int, splitted_time)
        total_seconds = minutes * 60 + seconds + milliseconds / 1000
        return total_seconds
    else:
        return None

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

    driver.refresh()  # Refresh Browser after login


driver.get(constant.LOGIN_URL)

# Load old session into the browser
if os.path.exists('cookies.json'):
    loadCookies()
    driver.get(constant.DASHBOARD_URL)
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

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "signUsername"))).send_keys(
            constant.LOGIN_EMAIL)

        wait = WebDriverWait(driver, 5)
        continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lv-btn-primary")))
        continue_button.click()
        time.sleep(5)
        # -------------
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))).send_keys(
            constant.LOGIN_PASSWORD)
        time.sleep(3)
        # -------------
        sign_in_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "lv_sign_in_panel_wide-primary-button")))
        sign_in_button.click()
        time.sleep(15)

        # After successful login save new session cookies ot json file
        saveCookies(driver)
    except Exception as e:
        if 'cookies.json' in os.listdir():
            os.remove("cookies.json")
            login(driver)


if constant.DASHBOARD_URL in driver.current_url:
    print('Previous session loaded')
else:
    login(driver)
    driver.get(constant.DASHBOARD_URL)

try:
    skip_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.guide-modal-footer-btn.guide-modal-footer-skip-btn')))
    skip_button.click()
    time.sleep(2)
except Exception as e:
    print("Skip button not found: ", e)

upload_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "cover-placeholder")))
upload_button.click()

# -------------
ok_button(constant.POPUP_XPATH)

# scroll down for filter
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "lv-tabs-down-icon"))).click()
print("scroll working.........")
time.sleep(5)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "side-tab-filter"))).click()
print("filter clicked.")

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "player-time")))
video_length_text = driver.find_element(By.CLASS_NAME, "player-time").text.strip().split("\n")[-1]
# print("video_length_block: ", video_length_block.text)
# video_length_text = video_length_block.find_elements(By.TAG_NAME, "span")[1].text
print("video_length_text: ", video_length_text)
video_length = round(text_to_seconds(video_length_text))
print("video_length: ", video_length)
element = driver.find_element(By.CLASS_NAME, "timeline-play-cursor-hd")
filter_pixel = (constant.for_1200_width_video_bar / video_length) * 3
print("filter_pixel: ", filter_pixel)
if filter_pixel < 10:
    filter_pixel = 10
number_of_filter = int(constant.for_1200_width_video_bar / filter_pixel)

# -------------------------------
for i in range(0, number_of_filter+1):
# for i in range(0, 1):
    text_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f"//*[text()='{constant.FILTER_NAME}']")))
    parent_element = text_element.find_element(By.XPATH, "..")
    parent_element.click()
    print("select filter")
    time.sleep(30)
    # ----scroll horizontal filter-----
      # filter time 3 sec
    # ActionChains(driver).click_and_hold(element).move_by_offset(constant.for_1200_width_video_bar, 0).release().perform()
    ActionChains(driver).click_and_hold(element).move_by_offset(filter_pixel, 0).release().perform()
    time.sleep(10)

# moving cursor to start
ActionChains(driver).click_and_hold(element).move_by_offset(-constant.for_1200_width_video_bar, 0).release().perform()
# ---------------------------------
time.sleep(60)
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/button"))).click()

ok_button(constant.POPUP_XPATH)

intensity_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, constant.BASIC_INTENSITY_XPATH)))
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
