import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pdfkit
#######################################
email = "armenbizz@gmail.com"
password = "1q2w3e"
#######################################


driver = webdriver.Chrome("%s/chromedriver" % os.path.dirname(os.path.abspath(__file__)))

driver.get("https://fabric.io/login")
time.sleep(1)

email_field = driver.find_element_by_xpath("//div[@class='sdk-form-control-group']/input[@id='email']")
email_field.send_keys(email)

pass_input = driver.find_element_by_xpath("//input[@id='password']")
pass_input.send_keys(password)

submit_button = driver.find_element_by_xpath("//button[@class='block sdk-button sign-in']")
submit_button.click()

time.sleep(1)
driver.get("https://fabric.io/panjur-bilisim/android/apps/com.heydate.android/dashboard")

time.sleep(2)
#pdfkit.from_string(driver.page_source, 'out.pdf')

driver.save_screenshot("screenshot.png")
