from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.reddit.com/report")

other_issues = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]')
other_issues.click()

time.sleep(2)

copyright_issues = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/h3')
copyright_issues.click()

time.sleep(2)

submit_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/button')
submit_btn.click()

time.sleep(3)

