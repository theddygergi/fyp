from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
import requests
from bs4 import BeautifulSoup
import speech_rec
import convert

delayTime = 2
audioToTextDelay = 10
filename = '1.mp3'
byPassUrl = 'https://www.google.com/recaptcha/api2/demo'

option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

def audioToText(mp3Path):
    newmp3=convert.convert_mp3_to_wav(mp3Path, "audio.wav")
    result=speech_rec.transcribe_wav("audio.wav")
    return result

def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)

driver = webdriver.Chrome(option)
driver.get(byPassUrl)
time.sleep(1)
googleClass = driver.find_elements(By.CLASS_NAME, 'g-recaptcha')[0]
time.sleep(2)
outeriframe = googleClass.find_element(By.TAG_NAME,'iframe')
time.sleep(1)
outeriframe.click()
time.sleep(2)
allIframesLen = driver.find_elements(By.TAG_NAME,'iframe')
time.sleep(1)
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
