import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import constant
import input

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
    color_saturation_input = WebDriverWait(driver, 5).until(
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
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "mask-exit-button-container"))).click()
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
    body_slim_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_SLIM_XPATH)))
    body_slim_input.send_keys(Keys.CONTROL, 'a')
    body_slim_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_SLIM)
    body_slim_input.send_keys(Keys.RETURN)
    #------------------
    body_legs_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_LEGS_XPATH)))
    body_legs_input.send_keys(Keys.CONTROL, 'a')
    body_legs_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_LEGS)
    body_legs_input.send_keys(Keys.RETURN)
    #------------------
    body_waist_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_WAIST_XPATH)))
    body_waist_input.send_keys(Keys.CONTROL, 'a')
    body_waist_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_WAIST)
    body_waist_input.send_keys(Keys.RETURN)
    #------------------
    body_head_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_HEAD_XPATH)))
    body_head_input.send_keys(Keys.CONTROL, 'a')
    body_head_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_HEAD)
    body_head_input.send_keys(Keys.RETURN)
    #------------------
    body_smooth_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_SMOOTH_XPATH)))
    body_smooth_input.send_keys(Keys.CONTROL, 'a')
    body_smooth_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_SMOOTH)
    body_smooth_input.send_keys(Keys.RETURN)
    #------------------
    body_brighten_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, constant.SMART_TOOLS_RETOUCH_BODY_BRIGHTEN_XPATH)))
    body_brighten_input.send_keys(Keys.CONTROL, 'a')
    body_brighten_input.send_keys(input.SMART_TOOLS_RETOUCH_BODY_BRIGHTEN)
    body_brighten_input.send_keys(Keys.RETURN)