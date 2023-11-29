import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# os.environ['PATH'] += "/home/alim/Documents/capcut/"

driver = webdriver.Chrome()
driver.get("https://www.capcut.com/login")

# driver.find_element('name', "signUsername").send_keys("alim.abdul.5915@gmail.com")

try:
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "signUsername")))
	element.send_keys("alim.abdul.5915@gmail.com")
except Exception as e:
	print(e)
wait = WebDriverWait(driver, 5)
continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lv-btn-primary")))
continue_button.click()
time.sleep(5)
#-------------
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("adminmilon")
time.sleep(3)
#-------------
sign_in_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lv_sign_in_panel_wide-primary-button")))
sign_in_button.click()
time.sleep(15)
#-------------
wait = WebDriverWait(driver, 2)
create_new_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "createNewButton--N83an")))
create_new_button.click()
time.sleep(2)
#-------------
wait = WebDriverWait(driver, 3)
_9_16_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "configItemTitle--skk7a")))
_9_16_button.click()
time.sleep(10)
#-------------
# Switch to the new tab
new_tab_handle = driver.window_handles[1]  # Assuming the new tab is the second window handle
driver.switch_to.window(new_tab_handle)
#-------------
# skip_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "guide-modal-footer-skip-btn")))
skip_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.guide-modal-footer-btn.guide-modal-footer-skip-btn')))
skip_button.click()
time.sleep(2)
#-------------
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
#-------------

# element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "side-tab-filter"))
# )

# element_to_scroll_to = driver.find_element(By.ID, "side-tab-filter")

# # Scroll to the element using the DOWN arrow key
# ActionChains(driver).move_to_element(element_to_scroll_to).send_keys(Keys.ARROW_DOWN).perform()

# # Now you can interact with the element if needed
# element_to_scroll_to.click()
# print("Scroll done")
#---------------

sidebar_panel = driver.find_element(By.CLASS_NAME, "lv-tabs-header-overflow-scroll")

# Create an ActionChains object to perform actions on the web page
actions = ActionChains(driver)

# Perform a series of actions to scroll the sidebar panel
actions.move_to_element(sidebar_panel)
actions.click_and_hold().move_by_offset(0, 100).release().perform()

element_to_scroll_to = driver.find_element(By.ID, "side-tab-filter")
element_to_scroll_to.click()
print("Scroll done")
#-------------
time.sleep(10)

driver.quit()
