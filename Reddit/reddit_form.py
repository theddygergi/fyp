from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.reddit.com/report")


email = driver.find_element(By.XPATH, '/html/body/shreddit-app/shreddit-overlay-display/span[4]/input')
email.send_keys("michael.me2@hotmail.com")

time.sleep(12)

password = driver.find_element(By.XPATH, '//*[@id="login-password"]')
password.send_keys("random1$A" + Keys.ENTER)

time.sleep(2)

WebDriverWait(driver, 12).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/shreddit-app/shreddit-overlay-display//shreddit-signup-drawer//shreddit-drawer/div/shreddit-async-loader/div/shreddit-slotter//span/shreddit-async-loader/auth-flow-login/faceplate-form/faceplate-tabpanel/auth-flow-modal[1]/div[2]'))
)
login = driver.find_element(By.XPATH, '/html/body/shreddit-app/shreddit-overlay-display//shreddit-signup-drawer//shreddit-drawer/div/shreddit-async-loader/div/shreddit-slotter//span/shreddit-async-loader/auth-flow-login/faceplate-form/faceplate-tabpanel/auth-flow-modal[1]/div[2]')
login.click()

time.sleep(15)

other_issues = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]')
other_issues.click()

time.sleep(2)

copyright_issues = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/h3')
copyright_issues.click()

time.sleep(2)

submit_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/button')
submit_btn.click()

time.sleep(3)

file_a_complaint = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/a')
file_a_complaint.click()

time.sleep(10)

cause = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/div/div/div/div[8]/div/form/div[1]/a')
cause.click()

time.sleep(3)

other_reports = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/div/div/div/div[8]/div/form/div[1]/a')
other_reports.click()

time.sleep(3)

email_address = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/div/div/div/div[8]/div/form/div[2]/input')
email_address.send_keys("marcelle.haddad@outook.com")

time.sleep(4)

report_type = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/div/div/div/div[8]/div/form/div[3]/a')
report_type.click()

time.sleep(3)

investigations = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/div/div/div/div[8]/div/form/div[5]')
investigations.click()

time.sleep(3)

sub_inquiry = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/div/div/div/div[8]/div/form/div[18]/input')
sub_inquiry.send_keys(" ")

time.sleep(2)

details_inquiry = driver.find_element(By.XPATH, '/html/body/p')
details_inquiry.send_keys(" ")

time.sleep(2)

checkbox = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/div/div/div/div[8]/div/form/div[29]/input[2]')
checkbox.click()

time.sleep(2)

submit_btn_2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/div/div/div/div[8]/div/form/footer/input')
submit_btn_2.click()



