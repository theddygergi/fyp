import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from speechToText import recognize_speech


# Function to save audio captcha file in the same directory as the script
def saveFile(content, filename):
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    file_path = os.path.join(script_directory, filename)  # Construct the absolute path to save the file
    with open(file_path, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)

# Create a new instance of the Chrome driver
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)

url = input("Please enter the URL: ")

# Navigate to the website
driver.get(url)

# Wait for the page to load completely (optional)
driver.implicitly_wait(10)  # Waits up to 10 seconds

# Switch to the iframe containing the reCAPTCHA widget
iframe = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="reCAPTCHA"]')))
driver.switch_to.frame(iframe)

# Find the reCAPTCHA checkbox element and click it
recaptcha_checkbox = driver.find_element(By.ID, 'recaptcha-anchor')
recaptcha_checkbox.click()

time.sleep(2)  # Wait for the audio button to load

# Locate the audio captcha button in iframes
allIframesLen = len(driver.find_elements(By.TAG_NAME,'div'))
audioBtnFound = False
audioBtnIndex = -1

# Iterate through all iframes to find the audio captcha button
for index in range(0, allIframesLen):
    driver.switch_to.default_content()
    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(5)
    try:
        # Find and click the audio captcha button
        audio_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'recaptcha-audio-button')))
        audio_btn.click()
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        pass

# If audio captcha button is found, proceed with solving the captcha
if audioBtnFound:
    try:
        # Generate a unique filename for saving the audio captcha file (e.g., using current timestamp)
        filename = f"audio_captcha_{int(time.time())}.mp3"

        while True:
            # Get the audio source URL
            href_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'audio')))
            href = href_element.get_attribute('src') if href_element else None
            if href:
                response = requests.get(href, stream=True)
                saveFile(response, filename)  # Save the audio captcha file
                response = recognize_speech(filename)  # Convert audio to text using speech recognition
                driver.switch_to.default_content()
                iframe = driver.find_elements(By.TAG_NAME, 'iframe')[audioBtnIndex]
                driver.switch_to.frame(iframe)
                inputbtn = driver.find_element(By.ID, 'audio-response')
                inputbtn.send_keys(response)
                inputbtn.send_keys(Keys.ENTER)
                time.sleep(2)
                errorMsg = driver.find_elements(By.CLASS_NAME, 'rc-audiochallenge-error-message')
                if errorMsg and len(errorMsg) > 0 and (errorMsg[0].text == "" or errorMsg[0].value_of_css_property('display') == 'none'):
                    print("Success")
                    
                    
                    break
                else:
                    print("Error: Invalid URL for audio captcha")
                    break
    except Exception as e:
        print(e)
        print('Caught. Need to change proxy now')
else:
    print('Audio Button not found.')

print("Captcha solved")