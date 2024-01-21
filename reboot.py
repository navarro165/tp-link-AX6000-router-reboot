#!/usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROUTER_IP = os.environ['ROUTER_REBOOT_IP']
USERNAME = os.environ['ROUTER_REBOOT_USERNAME']
PASSWORD = os.environ['ROUTER_REBOOT_PASSWORD']

def run(driver):
    driver.get(f'http://{ROUTER_IP}/webpages/index.html')
    driver.set_window_size(1247, 1095)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "TP-Link ID"))).click()
    driver.switch_to.frame(0)

    username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login_inputUser")))
    username_input.click()
    username_input.send_keys(USERNAME)

    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login_inputPassword")))
    password_input.click()
    password_input.send_keys(PASSWORD)
    driver.find_element(By.ID, "login_login").click()

    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Advanced"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "System"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Reboot"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "reboot-button"))).click()

    driver.quit()

try:
    driver = webdriver.Remote(command_executor='http://localhost:4444', options=webdriver.FirefoxOptions())
    run(driver)
except Exception as e:
    print(f"An error occurred: {e}")
    if driver:
        driver.quit()
finally:
    if driver:
        driver.quit()
