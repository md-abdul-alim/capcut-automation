# selenium 4
import os
from selenium import webdriver
import json
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import constant
import function

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1200,800")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#-------------------------Login Start-------------------
driver.get(constant.LOGIN_URL)
# Load old session into the browser
if os.path.exists('cookies.json'):
    function.loadCookies(driver)
    driver.get(constant.DASHBOARD_URL)

if constant.DASHBOARD_URL in driver.current_url:
    print('Previous session loaded')
else:
    function.login(driver)
    driver.get(constant.DASHBOARD_URL)
#-------------------------Login End-------------------

try:
    skip_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.guide-modal-footer-btn.guide-modal-footer-skip-btn')))
    skip_button.click()
    time.sleep(2)
except Exception as e:
    print("Skip button not found: ", e)

upload_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "cover-placeholder")))
upload_button.click()

# -------------
function.ok_button(driver=driver, xpath=constant.POPUP_XPATH)

# scroll down for filter
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "lv-tabs-down-icon"))).click()
print("scroll working.........")
time.sleep(5)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "side-tab-filter"))).click()
print("filter clicked.")

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "player-time")))
video_length_text = driver.find_element(By.CLASS_NAME, "player-time").text.strip().split("\n")[-1]
print("video_length_text: ", video_length_text)
video_length = round(function.text_to_seconds(video_length_text))
print("video_length: ", video_length)
element = driver.find_element(By.CLASS_NAME, "timeline-play-cursor-hd")
filter_pixel = (constant.FOR_1200_WIDTH_VIDEO_BAR / video_length) * 3
print("filter_pixel: ", filter_pixel)
if filter_pixel < 7:
    filter_pixel = 7
number_of_filter = int(constant.FOR_1200_WIDTH_VIDEO_BAR / filter_pixel)

# -------------------------------
# for i in range(0, number_of_filter + 1):
for i in range(0, 1):
    # for i in range(0, 1):
    text_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='{constant.FILTER_NAME}']")))
    parent_element = text_element.find_element(By.XPATH, "..")
    parent_element.click()
    print("select filter")
    if i == 0:
        time.sleep(15)
    else:
        time.sleep(2)
    # ----scroll horizontal filter-----
    # ActionChains(driver).click_and_hold(element).move_by_offset(constant.FOR_1200_WIDTH_VIDEO_BAR, 0).release().perform()
    ActionChains(driver).click_and_hold(element).move_by_offset(filter_pixel, 0).release().perform()
    time.sleep(2)

# moving cursor to start
ActionChains(driver).click_and_hold(element).move_by_offset(-constant.FOR_1200_WIDTH_VIDEO_BAR, 0).release().perform()
# ---------------------------------
time.sleep(10)
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/button"))).click()

function.ok_button(driver=driver, xpath=constant.POPUP_XPATH)
#-------------------------Basic input Start-------------------
function.basic_effect(driver)
#-------------------------Basic input End---------------------
#-------------------------Smart Tools input Start-------------
function.smart_tools_body_effect(driver)
#-------------------------Smart Tools input End---------------

time.sleep(995)
# close the browser
driver.quit()

print('Finished ...')
