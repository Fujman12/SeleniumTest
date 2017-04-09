import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from sendmail import sendmail
import datetime
#######################################
email = "armenbizz@gmail.com"
password = "1q2w3e"
#######################################


def run_driver():
    print("Starting Selenium Webdriver...")
    driver = webdriver.PhantomJS("%s/phantomjs_Linux32" % os.path.dirname(os.path.abspath(__file__)))

    # hack while the python interface lags
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')

    print("Going to fabric.io...")
    driver.get("https://fabric.io/login")
    time.sleep(1)

    email_field = driver.find_element_by_xpath("//div[@class='sdk-form-control-group']/input[@id='email']")
    email_field.send_keys(email)

    pass_input = driver.find_element_by_xpath("//input[@id='password']")
    pass_input.send_keys(password)

    submit_button = driver.find_element_by_xpath("//button[@class='block sdk-button sign-in']")
    submit_button.click()
    print("Loged in. Going to dashboard...")
    time.sleep(1)
    driver.get("https://fabric.io/panjur-bilisim/android/apps/com.heydate.android/dashboard")

    return driver

def get_pdf():
    #pdfkit.from_string(driver.page_source, 'out.pdf')
    driver = run_driver()
    driver.maximize_window()
    time.sleep(3)
    # set page format
    # inside the execution script, webpage is "this"
    pageFormat = '''this.paperSize = {format: "A1", orientation: "landscape" };'''
    driver.execute('executePhantomScript', {'script': pageFormat, 'args' : [] })

    # render current page
    print("Getting the pdf...")
    render = """this.render("test_%s.pdf")""" % datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    driver.execute('executePhantomScript', {'script': render, 'args' : [] })

    driver.quit()

get_pdf()
sendmail()
