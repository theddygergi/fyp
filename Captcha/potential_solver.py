from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com/recaptcha/api2/demo')

not_bot_btn = driver.find_element(By.CLASS_NAME, '/html/body/div[2]/div[3]/div[2]/div/label/span')
not_bot_btn.click()



