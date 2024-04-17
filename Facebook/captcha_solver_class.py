from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
import requests
import speech_rec
import convert

class CaptchaSolver:
    def __init__(self):
        self.delayTime = 2
        self.audioToTextDelay = 10
        self.filename = '1.mp3'
        self.byPassUrl = 'https://www.google.com/recaptcha/api2/demo'
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--disable-notifications')
        self.option.add_argument("--mute-audio")
        self.option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
        self.driver = webdriver.Chrome(options=self.option)

    def audioToText(self, mp3Path):
        newmp3=convert.convert_mp3_to_wav(mp3Path, "audio.wav")
        result=speech_rec.transcribe_wav("audio.wav")
        return result

    def saveFile(self, content, filename):
        with open(filename, "wb") as handle:
            for data in content.iter_content():
                handle.write(data)

    def solveCaptcha(self):
        #self.driver.get(self.byPassUrl)
        #time.sleep(1)
        googleClass = self.driver.find_elements(By.CLASS_NAME, 'g-recaptcha')[0]
        time.sleep(2)
        outeriframe = googleClass.find_element(By.TAG_NAME,'iframe')
        time.sleep(1)
        outeriframe.click()
        time.sleep(2)
        allIframesLen = self.driver.find_elements(By.TAG_NAME,'iframe')
        time.sleep(1)
        audioBtnFound = False
        audioBtnIndex = -1

        for index in range(len(allIframesLen)):
            self.driver.switch_to.default_content()
            iframe = self.driver.find_elements(By.TAG_NAME,'iframe')[index]
            self.driver.switch_to.frame(iframe)
            self.driver.implicitly_wait(self.delayTime)
            try:
                audioBtn = self.driver.find_element(By.ID,'recaptcha-audio-button') or self.driver.find_element(By.ID,'recaptcha-anchor')
                audioBtn.click()
                audioBtnFound = True
                audioBtnIndex = index
                break
            except Exception as e:
                pass

        if audioBtnFound:
            try:
                while True:
                    href = self.driver.find_element(By.ID,'audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    self.saveFile(response,self.filename)
                    response = self.audioToText(os.getcwd() + '/' + self.filename)
                    print(response)
                    self.driver.switch_to.default_content()
                    iframe = self.driver.find_elements(By.TAG_NAME,'iframe')[audioBtnIndex]
                    self.driver.switch_to.frame(iframe)
                    inputbtn = self.driver.find_element(By.ID,'audio-response')
                    inputbtn.send_keys(response)
                    inputbtn.send_keys(Keys.ENTER)
                    time.sleep(2)
                    errorMsg = self.driver.find_elements(By.CLASS_NAME,'rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        break
            except Exception as e:
                print(e)
        else:
            print('Button not found. This should not happen.')

# Example usage:
solver = CaptchaSolver()
solver.solveCaptcha()
