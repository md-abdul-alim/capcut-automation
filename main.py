# selenium 4
import os
import json
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from pydantic import BaseModel
import time
import constant
import input

def get_options():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # options.add_argument("--single-process")
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--disable-web-security')
    # options.add_argument('--disable-features=IsolateOrigins,site-per-process')
    # options.add_argument('--disable-extensions')
    options.add_argument("--window-size=1200,800")
    options.add_argument(f'--user-agent={headers["User-Agent"]}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # # add page load strategy to none
    # options.page_load_strategy = 'none'

    return options


def config_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=get_options())
    return driver

driver = config_driver()
driver.get(constant.LOGIN_URL)

def saveCookies(driver):
    cookies = driver.get_cookies()

    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print('New Cookies saved successfully')

def loadCookies(driver):
    if 'cookies.json' in os.listdir():

        with open('cookies.json', 'r') as file:
            cookies = json.load(file)

        for cookie in cookies:
            driver.add_cookie(cookie)
    else:
        print('No cookies file found')

    driver.refresh()  # Refresh Browser after login

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

def ok_button(driver, xpath):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"{xpath}"))).click()
        time.sleep(2)
        print("ok button")
    except Exception as e:
        print("Ok button error: ", e)

def text_to_seconds(time_text):
    # Use regular expression to extract hours, minutes, seconds, and milliseconds
    splitted_time = time_text.split(':')

    if len(splitted_time) == 3:
        minutes, seconds, milliseconds = map(int, splitted_time)
        total_seconds = minutes * 60 + seconds + milliseconds / 1000
        return total_seconds
    else:
        return None
    
def open_filter_and_search(driver):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "lv-tabs-down-icon"))).click()
    print("scroll working.........")
    time.sleep(3)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "side-tab-filter"))).click()
    print("filter clicked.")
    time.sleep(5)
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.FILTER_TYPE_EXPAND_XPATH))).click()
        print('filter type expand')
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.FILTER_DICT_WITH_EXPAND[constant.FILTER_TYPE]))).click()
        print('filter type clicked')
        time.sleep(7)
    except Exception as e:
        print('except block')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.FILTER_DICT_WITHOUT_EXPAND[constant.FILTER_TYPE]))).click()
        print('filter type clicked')
        time.sleep(7)

def basic_effect(driver):
    intensity_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, constant.BASIC_INTENSITY_XPATH)))
    intensity_input.send_keys(Keys.CONTROL, 'a')
    intensity_input.send_keys(input.BASIC_INTENSITY_VALUE)
    intensity_input.send_keys(Keys.RETURN)
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "segment-widget"))).click()
    #------------------
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.BASIC_COLOR_ADJUSTMENT_XPATH))).click()
    color_saturation_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_COLOR_ADJUSTMENT_COLOR_SATURATION_XPATH)))
    color_saturation_input.send_keys(Keys.CONTROL, 'a')
    color_saturation_input.send_keys(input.BASIC_COLOR_ADJUSTMENT_COLOR_SATURATION)
    color_saturation_input.send_keys(Keys.RETURN)
    #------------------
    color_temperature_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_COLOR_ADJUSTMENT_COLOR_TEMPERATURE_XPATH)))
    color_temperature_input.send_keys(Keys.CONTROL, 'a')
    color_temperature_input.send_keys(input.BASIC_COLOR_ADJUSTMENT_COLOR_TEMPERATURE)
    color_temperature_input.send_keys(Keys.RETURN)
    #------------------
    color_brightness_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_BRIGHTNESS_XPATH)))
    color_brightness_input.send_keys(Keys.CONTROL, 'a')
    color_brightness_input.send_keys(input.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_BRIGHTNESS)
    color_brightness_input.send_keys(Keys.RETURN)
    #------------------
    color_contrast_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_CONTRAST_XPATH)))
    color_contrast_input.send_keys(Keys.CONTROL, 'a')
    color_contrast_input.send_keys(input.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_CONTRAST)
    color_contrast_input.send_keys(Keys.RETURN)
    #------------------
    color_shine_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_SHINE_XPATH)))
    color_shine_input.send_keys(Keys.CONTROL, 'a')
    color_shine_input.send_keys(input.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_SHINE)
    color_shine_input.send_keys(Keys.RETURN)
    #------------------
    color_highlight_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_HIGHLIGHT_XPATH)))
    color_highlight_input.send_keys(Keys.CONTROL, 'a')
    color_highlight_input.send_keys(input.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_HIGHLIGHT)
    color_highlight_input.send_keys(Keys.RETURN)
    #------------------
    color_shadow_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_SHADOW_XPATH)))
    color_shadow_input.send_keys(Keys.CONTROL, 'a')
    color_shadow_input.send_keys(input.BASIC_COLOR_ADJUSTMENT_LIGHTNESS_SHADOW)
    color_shadow_input.send_keys(Keys.RETURN)
    #------------------
    effect_sharpness_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_EFFECT_SHARPNESS_XPATH)))
    effect_sharpness_input.send_keys(Keys.CONTROL, 'a')
    effect_sharpness_input.send_keys(input.BASIC_EFFECT_SHARPNESS)
    effect_sharpness_input.send_keys(Keys.RETURN)
    #------------------
    effect_vignette_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_EFFECT_VIGNETTE_XPATH)))
    effect_vignette_input.send_keys(Keys.CONTROL, 'a')
    effect_vignette_input.send_keys(input.BASIC_EFFECT_VIGNETTE)
    effect_vignette_input.send_keys(Keys.RETURN)
    #------------------
    effect_fade_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_EFFECT_FADE_XPATH)))
    effect_fade_input.send_keys(Keys.CONTROL, 'a')
    effect_fade_input.send_keys(input.BASIC_EFFECT_FADE)
    effect_fade_input.send_keys(Keys.RETURN)
    #------------------
    effect_grain_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_EFFECT_GRAIN_XPATH)))
    effect_grain_input.send_keys(Keys.CONTROL, 'a')
    effect_grain_input.send_keys(input.BASIC_EFFECT_GRAIN)
    effect_grain_input.send_keys(Keys.RETURN)
    #------------------
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "mask-exit-button-container"))).click()
    #------------------
    blend_opacity_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_BLEND_OPACITY_XPATH)))
    blend_opacity_input.send_keys(Keys.CONTROL, 'a')
    blend_opacity_input.send_keys(input.BASIC_BLEND_OPACITY)
    blend_opacity_input.send_keys(Keys.RETURN)
    #------------------
    transform_scale_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_TRANSFORM_SCALE_XPATH)))
    transform_scale_input.send_keys(Keys.CONTROL, 'a')
    transform_scale_input.send_keys(input.BASIC_TRANSFORM_SCALE)
    transform_scale_input.send_keys(Keys.RETURN)
    #------------------
    transform_position_x_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_TRANSFORM_POSITION_X_XPATH)))
    transform_position_x_input.send_keys(Keys.CONTROL, 'a')
    transform_position_x_input.send_keys(input.BASIC_TRANSFORM_POSITION_X)
    transform_position_x_input.send_keys(Keys.RETURN)
    #------------------
    transform_position_y_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_TRANSFORM_POSITION_Y_XPATH)))
    transform_position_y_input.send_keys(Keys.CONTROL, 'a')
    transform_position_y_input.send_keys(input.BASIC_TRANSFORM_POSITION_Y)
    transform_position_y_input.send_keys(Keys.RETURN)
    #------------------
    transform_rotate_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.BASIC_TRANSFORM_ROTATE_XPATH)))
    transform_rotate_input.send_keys(Keys.CONTROL, 'a')
    transform_rotate_input.send_keys(input.BASIC_TRANSFORM_ROTATE)
    transform_rotate_input.send_keys(Keys.RETURN)


def smart_tools_body_effect(driver):
    print('Scroll the time you want to use body shape effect: ')
    # time.sleep(15)
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_XPATH))).click()
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_XPATH))).click()
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_XPATH))).click()
    #------------------
    body_slim_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_SLIM_XPATH)))
    body_slim_input.send_keys(Keys.CONTROL, 'a')
    body_slim_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_SLIM)
    body_slim_input.send_keys(Keys.RETURN)
    #------------------
    body_legs_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_LEGS_XPATH)))
    body_legs_input.send_keys(Keys.CONTROL, 'a')
    body_legs_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_LEGS)
    body_legs_input.send_keys(Keys.RETURN)
    #------------------
    body_waist_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_WAIST_XPATH)))
    body_waist_input.send_keys(Keys.CONTROL, 'a')
    body_waist_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_WAIST)
    body_waist_input.send_keys(Keys.RETURN)
    #------------------
    body_head_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_HEAD_XPATH)))
    body_head_input.send_keys(Keys.CONTROL, 'a')
    body_head_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_HEAD)
    body_head_input.send_keys(Keys.RETURN)
    #------------------
    body_smooth_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_SMOOTH_XPATH)))
    body_smooth_input.send_keys(Keys.CONTROL, 'a')
    body_smooth_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_SMOOTH)
    body_smooth_input.send_keys(Keys.RETURN)
    #------------------
    body_brighten_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_BRIGHTEN_XPATH)))
    body_brighten_input.send_keys(Keys.CONTROL, 'a')
    body_brighten_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_BRIGHTEN)
    body_brighten_input.send_keys(Keys.RETURN)

def download_function(driver):
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, constant.EXPORT_BUTTON))).click()
    time.sleep(3)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, constant.DOWNLOAD_BUTTON))).click()
    time.sleep(3)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, constant.CONFIRM_EXPORT_BUTTON))).click()
    #----------------------

    # Wait until the Download button is present
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, "downloadButton"))
    ).click()
    time.sleep(5)
    print("Download button clicked!")
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[12]/div[2]/div/div/div[1]/div[2]/svg[2]"))
    ).click()
    # Click on the second <svg> element (index 1, as indexing starts from 0)
    # svg_elements[1].click()
    print("Download button closed!")
    time.sleep(5)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lv-btn-shape-square"))
    ).click()
    
#-------------------------Login Start-------------------

#-------------------------Login End-------------------


# -------------
def video_length_pixel_calculation(driver):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "player-time")))
    video_length_text = driver.find_element(By.CLASS_NAME, "player-time").text.strip().split("\n")[-1]
    print("video_length_text: ", video_length_text)
    video_length = round(text_to_seconds(video_length_text))
    print("video_length: ", video_length)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "timeline-play-cursor-hd")))
    element = driver.find_element(By.CLASS_NAME, "timeline-play-cursor-hd")
    filter_pixel = (constant.FOR_1200_WIDTH_VIDEO_BAR / video_length) * 3
    print("filter_pixel: ", filter_pixel)
    if filter_pixel < 7:
        filter_pixel = 7
    number_of_filter = int(constant.FOR_1200_WIDTH_VIDEO_BAR / filter_pixel)
    return element, filter_pixel, number_of_filter

def horizontal_scroll_movement(driver, element, filter_pixel, number_of_filter):
    # for i in range(0, number_of_filter + 1):
    for i in range(0, 1):
        # for i in range(0, 1):
        text_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='{constant.FILTER_NAME}']")))
        parent_element = text_element.find_element(By.XPATH, "..")
        parent_element.click()
        print("select filter")
        if i == 0:
            time.sleep(30)
        else:
            time.sleep(1)
        # ----scroll horizontal filter-----
        # ActionChains(driver).click_and_hold(element).move_by_offset(constant.FOR_1200_WIDTH_VIDEO_BAR, 0).release().perform()
        ActionChains(driver).click_and_hold(element).move_by_offset(filter_pixel, 0).release().perform()
        time.sleep(1)
    # moving cursor to start
    ActionChains(driver).click_and_hold(element).move_by_offset(-(constant.FOR_1200_WIDTH_VIDEO_BAR + 100), 0).release().perform()
    time.sleep(10)

def start_login(driver):
    if os.path.exists('cookies.json'):
        loadCookies(driver)
        driver.get(constant.DASHBOARD_URL)

    if constant.DASHBOARD_URL in driver.current_url:
        print('Previous session loaded')
    else:
        login(driver)
        driver.get(constant.DASHBOARD_URL)

def skip_click(driver):
        try:
            skip_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button.guide-modal-footer-btn.guide-modal-footer-skip-btn')))
            skip_button.click()
            time.sleep(2)
        except Exception as e:
            print("Skip button not found: ", e)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "cover-placeholder"))).click()

def main():
    #------------Login Start------------
    start_login(driver)
    #-------------Login End-----------
    skip_click(driver)

    ok_button(driver=driver, xpath=constant.POPUP_XPATH)

    # get all video title list
    parent_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="virtuoso-item-list"]'))
    )
    elements = parent_div.find_elements(By.CLASS_NAME, 'card-item-label')
    data_list = [element.text for element in elements]
    print(data_list)

    element, filter_pixel, number_of_filter = video_length_pixel_calculation(driver) # Select Video

    open_filter_and_search(driver)

    horizontal_scroll_movement(driver, element, filter_pixel, number_of_filter)

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/button"))).click()

    ok_button(driver=driver, xpath=constant.POPUP_XPATH)

    basic_effect(driver)

    smart_tools_body_effect(driver)

    ok_button(driver=driver, xpath='/html/body/div[9]/div[4]/div/button')

    download_function(driver)

    time.sleep(995)
    # close the browser
    driver.quit()

    print('Finished ...')


main()