from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import out_op
import requests
import os
import convert
import speech_rec
#from captcha_solver_class import CaptchaSolver
def audioToText(mp3Path):
    newmp3=convert.convert_mp3_to_wav(mp3Path, "audio.wav")
    result=speech_rec.transcribe_wav("audio.wav")
    return result

def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)

filename = '1.mp3'
delayTime = 2

option = uc.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

driver = uc.Chrome(option)
driver.get("https://facebook.com")

#WebDriverWait(driver, 15).until(
#    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]'))
#)
#
#allow_cookies = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]')
#allow_cookies.click()


# Find email and password fields and enter credentials
email_element = driver.find_element(By.ID, "email")
password_element = driver.find_element(By.ID, "pass")
email_element.send_keys("marcelle.haddad@outlook.com")
password_element.send_keys("marcelle1q2w3e4r5t")

# Click on the login button
login_element = driver.find_element(By.NAME, "login")
login_element.click()

# Wait for some time to simulate a user interaction (you may adjust this)
time.sleep(5)

# Perform any actions needed after login
driver.get("https://www.facebook.com/help/contact/copyrightform")

# Find and click the copy button
btn_copy = driver.find_element(By.XPATH, '//*[@id="SupportFormRow.250116565117827"]/div[3]/label[1]/span')
btn_copy.click()

# Wait for elements to load
time.sleep(2)

# Fill in the email confirmation
conf_email = driver.find_element(By.XPATH, '//*[@id="755605467935533"]')
conf_email.send_keys("marcelle.haddad@outlook.com")

# Wait for elements to load
time.sleep(4)

# Select the country
countries = driver.find_element(By.XPATH, '//*[@id="645486236964608"]')
countries.click()

# Wait for elements to load
time.sleep(2)

# Select Lebanon as the country
leb_country = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[12]/select/option[121]')
leb_country.click()

# Wait for elements to load
time.sleep(3)

# Select the category
category = driver.find_element(By.XPATH, '//*[@id="418475341579315"]')
category.click()

# Wait for elements to load
time.sleep(2)

# Select Photo/Video as the category
photo_opt = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[13]/select/option[2]')
photo_opt.click()

# Wait for elements to load
time.sleep(2)

# Enter the name of the person who copied the work
name_copy = driver.find_element(By.XPATH, '//*[@id="1467491100178767"]')
name_copy.send_keys("Emilio Dandan")

# Wait for elements to load
time.sleep(3)

# Click on the checkbox for the photo/video
photo_click = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[15]/div[2]/label[1]/span')
photo_click.click()

# Wait for elements to load
time.sleep(2)

# Enter the URL of the photo/video
photo_url = driver.find_element(By.XPATH, '//*[@id="173734026110493"]')
photo_url.send_keys("https://www.facebook.com/photo/?fbid=122102856158249533&set=a.1221028562062495334")

# Wait for elements to load
time.sleep(4)

# Enter the URL of the photo/video again
photo_url2 = driver.find_element(By.XPATH, '//*[@id="388149281267730"]')
photo_url2.send_keys("https://www.facebook.com/photo/?fbid=122102856158249533&set=a.1221028562062495334")

# Wait for elements to load
time.sleep(4)

# Select the reason for reporting
reason = driver.find_element(By.XPATH, '//*[@id="136284146523176"]')
reason.click()

# Wait for elements to load
time.sleep(4)

# Select the option for copies work
copies_work = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[27]/select/option[2]')
copies_work.click()

# Wait for elements to load
time.sleep(4)

# Add additional information
add_info = driver.find_element(By.XPATH , '//*[@id="451242651624945"]')
add_info.send_keys("The facebook account Michael Merri posted one of my profile pictures to his facebook feed without asking my permission. Please consider this report")

# Wait for elements to load
time.sleep(6)

# Enter your signature
ele_signature = driver.find_element(By.XPATH , '//*[@id="159694930852744"]')
ele_signature.send_keys("Marcelle Haddad")

# Click on the submit button
submit_btn = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[3]/div/button')
submit_btn.click()

# Wait for elements to load
time.sleep(10)

# Bypass captcha and OTP
input_otp = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[2]/div[2]/div/input")
time.sleep(10)
OTP_code = out_op.get_outlook_otp("marcelle.haddad@outlook.com", "marcelle1q2w3e4r5t")
time.sleep(10)
input_otp.send_keys(OTP_code)

# Click on the confirm button
confirm_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[3]/button")
confirm_button.click()

time.sleep(5000)

# your existing code

# Get all window handles
all_handles = driver.window_handles

# Iterate through each window handle
for handle in all_handles:
    try:
        # Switch to the window
        driver.switch_to.window(handle)
        
        # Check if the reCAPTCHA element is present
        googleClass = driver.find_element(By.CLASS_NAME, 'g-recaptcha')

        break
    except Exception:
        continue
else:
    print("Error: Could not find the reCAPTCHA element in any window")

 

googleClass = driver.find_element(By.CLASS_NAME, 'g-recaptcha')
time.sleep(4)
outeriframe = googleClass.find_element(By.TAG_NAME,'iframe')
time.sleep(2)
outeriframe.click()
time.sleep(4)
allIframesLen = driver.find_elements(By.TAG_NAME,'iframe')
time.sleep(2)
audioBtnFound = False
audioBtnIndex = -1

for index in range(len(allIframesLen)):
    driver.switch_to.default_content()
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)
    try:
        audioBtn = driver.find_element(By.ID,'recaptcha-audio-button') or driver.find_element(By.ID,'recaptcha-anchor')
        audioBtn.click()
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        pass

if audioBtnFound:
    try:
        while True:
            href = driver.find_element(By.ID,'audio-source').get_attribute('src')
            response = requests.get(href, stream=True)
            saveFile(response,filename)
            response = audioToText(os.getcwd() + '/' + filename)
            print(response)
            driver.switch_to.default_content()
            iframe = driver.find_elements(By.TAG_NAME,'iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)
            inputbtn = driver.find_element(By.ID,'audio-response')
            inputbtn.send_keys(response)
            inputbtn.send_keys(Keys.ENTER)
            time.sleep(2)
            errorMsg = driver.find_elements(By.CLASS_NAME,'rc-audiochallenge-error-message')[0]
            if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                print("Success")
                break
    except Exception as e:
        print(e)
else:
    print('Button not found. This should not happen.')


#captcha_solver = CaptchaSolver()
#captcha_solver.solveCaptcha()

# Close the driver
driver.quit()
