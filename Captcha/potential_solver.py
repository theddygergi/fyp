from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/recaptcha/api2/demo')
time.sleep(5)

# Switch to the reCAPTCHA iframe
recaptcha_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='recaptcha']")
driver.switch_to.frame(recaptcha_iframe)

# Click the reCAPTCHA checkbox
checkbox = driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border")
checkbox.click()

# Wait for the audio challenge button to be present and clickable
audio_challenge_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "recaptcha-audio-button"))
)

# Click the audio challenge button
audio_challenge_button.click()

# Wait for the audio challenge to load
audio_source = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "audio-source"))
)

# Get the audio source URL
audio_url = audio_source.get_attribute("src")

# Handle the audio challenge
# ...
# (Additional code to handle the audio challenge using the audio_url)

# Switch back to the default content
driver.switch_to.default_content()