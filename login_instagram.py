from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.instagram.com/")

time.sleep(2)

username=browser.find_element_by_name("username")

username.send_keys("enter your username here") 

password=browser.find_element_by_name("password") 

password.send_keys("enter your password here") 

login=browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button")

login.click()

time.sleep(2)

close_notifications=browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")

close_notifications.click()

time.sleep(2)
