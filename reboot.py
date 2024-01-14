#!/usr/bin/env python3

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


ROUTER_IP = os.environ['ROUTER_REBOOT_IP']
USERNAME = os.environ['ROUTER_REBOOT_USERNAME']
PASSWORD = os.environ['ROUTER_REBOOT_PASSWORD']


driver = None


def run():
    driver = webdriver.Remote(command_executor='http://localhost:4444', options=webdriver.FirefoxOptions())
    driver.get(f'http://{ROUTER_IP}/webpages/index.html')
    driver.set_window_size(1247, 1095)

    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "TP-Link ID").click()

    time.sleep(3)
    driver.switch_to.frame(0)

    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) .input-group").click()
    driver.find_element(By.ID, "login_inputUser").send_keys(USERNAME)

    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".has-feedback").click()
    driver.find_element(By.ID, "login_inputPassword").send_keys(PASSWORD)
    driver.find_element(By.ID, "login_login").click()

    time.sleep(3)
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, "Advanced").click()

    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "System").click()

    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Reboot").click()

    time.sleep(5)
    driver.find_element(By.ID, "reboot-button").click()

    time.sleep(5)
    driver.quit()


try:
    run()
except Exception:  # try again
    if driver is not None:
        driver.quit()
    time.sleep(5)
    run()
finally:
    if driver is not None:
        driver.quit()
