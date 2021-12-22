# -*- coding: utf-8 -*-
"""
Created on Thu May 13 01:01:23 2021

@author: Alexander Merolla

This is just an example program I made to order Pad Thai from
my favorite resturant. It's simple and straightforward. Use it
as an example of the Python Selenium library if you wish.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Enter your login details here
myuser = 'place-username'
mypass = 'place-password'

# Function to wait for an xpath to become clickable
def wait_for_click(driver, xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
            )
        return element
    except:
        # Let's just try again
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
            )
        return element

# Functionm to wait for an xpath to load
def wait_for_element(driver, xpath):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
        )
    return element

# Set Chrome as browser
driver = webdriver.Chrome()
# Get the website
driver.get('http://tongphoonri.com/')
# Find the menu link and go there
whereclick = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[2]/a')
driver.get(whereclick.get_attribute('href'))
# Wait for redirect
whereclick = wait_for_click(driver, '//*[@id="modalAnnounce"]/div/div/div/div[2]/div/button/span/i')
# Close the information pop-up
whereclick.click()
# Find and click the login button
whereclick = wait_for_click(driver, '//*[@id="koMenuView"]/div/div[1]/nav/div[2]/div/ul/li[1]/a')
whereclick.click()
# Enter login details
field = wait_for_click(driver, '//*[@id="txtLogInEmail"]')
field.send_keys(myuser)
field = driver.find_element_by_xpath('//*[@id="txtLogInPassword"]')
field.send_keys(mypass)
# Click login
whereclick = driver.find_element_by_xpath('//*[@id="frmLogIn"]/div[5]/div/button/span')
whereclick.click()
# Get rid of popup
whereclick = wait_for_click(driver, '/html/body/div[46]/div/div[10]/button[1]')
whereclick.click()
# Select time (second div element for next closest time)
whereclick = wait_for_click(driver, '//*[@id="menuHourDay"]/div/div/input')
whereclick.click()
whereclick = wait_for_click(driver, '/html/body/div[46]/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div')
whereclick.click()
# Add food to cart
# Victoria's order
whereclick = wait_for_click(driver, '//*[@id="1_4"]/div/div/div[1]/a/dl/dt/span[1]/span')
whereclick.click()
# Select 1 spicy
whereclick = wait_for_click(driver, '/html/body/div[31]/div[2]/div[2]/div/div[8]/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div/div/div/input')
driver.execute_script("arguments[0].click();", whereclick)
whereclick = wait_for_click(driver, '/html/body/div[46]/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div')
driver.execute_script("arguments[0].click();", whereclick)
# Select Gluten Free
whereclick = driver.find_element_by_xpath('/html/body/div[31]/div[2]/div[2]/div/div[8]/div/div/div[2]/div[2]/div[4]/div[1]/div[9]/div/div/div[1]/input')
driver.execute_script("arguments[0].click();", whereclick)
field = driver.find_element_by_xpath('//*[@id="modalFood"]/div/div/div[2]/div[2]/div[4]/div[2]/div')
tryactions = ActionChains(driver)
tryactions.move_to_element(field)
tryactions.perform()
# Special instructions
field.send_keys('No scallions and less sauce please.')
# Add to cart
whereclick = wait_for_click(driver, '//*[@id="modalFood"]/div/div/div[3]/button[2]/span')
whereclick.click()
