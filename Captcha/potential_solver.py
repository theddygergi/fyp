from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com/recaptcha/api2/demo')

time.sleep(5)

recaptcha_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha']")
driver.switch_to.frame(recaptcha_iframe)

# Find and click on the reCAPTCHA checkbox
checkbox = driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border")
checkbox.click()

# Wait for the audio button to be clickable
audio_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[2]')))
audio_button.click()

# Switch back to the default content
driver.switch_to.default_content()

#still need to 
