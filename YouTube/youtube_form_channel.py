from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc

driver=uc.Chrome()
driver.get('https://studio.youtube.com/channel/UCbPWlmdoVIiRpomlDEIrvVQ/copyright/history')

time.sleep(3)

google_email=driver.find_element(By.XPATH, '//*[@id="identifierId"]')
google_email.send_keys('bahsa.leb@gmail.com')

time.sleep(3)

Next_button=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span')
Next_button.click()

time.sleep(5)

password = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password.send_keys("1q2w3e4r5t!@#$%")

time.sleep(5)

next_btn2 = driver.find_element(By.XPATH , '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span')
next_btn2.click()

time.sleep(5)

#not_now = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz[2]/div/div/div/div[2]/div[4]/div[1]/button/span')
#not_now.click()

#time.sleep(5)

return_to_studio = driver.find_element(By.XPATH, '/html/body/div[2]/p[5]/a')
return_to_studio.click()

time.sleep(5)

#create_channel = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div/div[6]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
#create_channel.click()

#time.sleep(5)

#continue_btn = driver.find_element(By.XPATH, '/html/body/ytcp-warm-welcome-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-button/div')
#continue_btn.click()

#time.sleep(5)

copyright_btn = driver.find_element(By.CSS_SELECTOR, '#menu-item-5')
copyright_btn.click()

time.sleep(5)

new_removal = driver.find_element(By.XPATH, '/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[22]/ytcr-management-page/ytcr-management-section/ytcp-primary-action-bar/div/span/ytcp-button/div')
new_removal.click()

time.sleep(5)

opt1_add_vid = driver.find_element(By.XPATH, '//*[@id="add-new-entry"]')
opt1_add_vid.click()

time.sleep(2)

opt1_select = driver.find_element(By.CSS_SELECTOR ,'')
opt1_add_vid.click()

time.sleep(5)

other_opt = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[2]/div[2]/ytcr-manual-entry/div[2]/div/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[2]')
other_opt.click()

time.sleep(4)

type_copyright = driver.find_element(By.XPATH, '//*[@id="otherIssue"]/div/textarea')
type_copyright.send_keys("Stealing")

time.sleep(4)

title_copyright = driver.find_element(By.XPATH, '//*[@id="title"]/div/textarea')
title_copyright.send_keys("Stealing")

time.sleep(5)

add_info = driver.find_element(By.XPATH, '//*[@id="description"]/div/textarea')
add_info.send_keys("A yt channel stole my content")

time.sleep(5)

url = driver.find_element(By.XPATH, '//*[@id="targetVideo"]/div/textarea')
url.send_keys("https://www.youtube.com/watch?v=m38wK-Xd6mo")

time.sleep(5)

aff_party = driver.find_element(By.XPATH , '//*[@id="right-icon"]')
aff_party.click()

time.sleep(5)

aff_party_opt = driver.find_element(By.XPATH, '//*[@id="text-item-1"]/ytcp-ve/tp-yt-paper-item-body/div/div/div/yt-formatted-string')
aff_party_opt.click()

time.sleep(5)

copyright_owner_name = driver.find_element(By.XPATH , '//*[@id="claimant-name"]/div/textarea')
copyright_owner_name.send_keys("xxx")

time.sleep(5)

phone_number = driver.find_element(By.XPATH, '//*[@id="phone"]/div/textarea')
phone_number.send_keys("+995577208104")

time.sleep(5)

rel_to_copyrighted = driver.find_element(By.XPATH, '//*[@id="requester-authority"]/div/textarea')
rel_to_copyrighted.send_keys("My fazer")

time.sleep(5)

country = driver.find_element(By.XPATH, '//*[@id="trigger"]/ytcp-dropdown-trigger/div/div[3]')
country.click()

time.sleep(2)

leb_select = driver.find_element(By.XPATH, '//*[@id="text-item-128"]/ytcp-ve/tp-yt-paper-item-body/div/div/div/yt-formatted-string')
leb_select.click()

time.sleep(3)

street_address = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[3]/div[2]/div[8]/ytcp-form-textarea/div/textarea')
street_address.send_keys("Hay el Sellom")

time.sleep(5)

city = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[3]/div[2]/div[9]/ytcp-form-textarea/div/textarea')
city.send_keys("Beirut")

time.sleep(5)

state = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[3]/div[2]/div[10]/div[1]/ytcp-form-textarea[1]/div/textarea')
state.send_keys("Mount Lebanon")

time.sleep(5)

postcode = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[3]/div[2]/div[10]/div[1]/ytcp-form-textarea[2]/div/textarea')
postcode.send_keys("00000")

time.sleep(5)

radio_btn = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[4]/ytcr-takedown-options/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]')
radio_btn.click()

time.sleep(2)

future_prevent = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[4]/ytcr-takedown-options/ytcp-form-checkbox/ytcp-checkbox-lit/div/div[1]/div/div')
future_prevent.click()

time.sleep(3)

opt1 = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[5]/div[2]/div[1]/ytcp-form-checkbox[1]/ytcp-checkbox-lit/div/div[1]/div/div')
opt1.click()

opt2 = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[5]/div[2]/div[1]/ytcp-form-checkbox[2]/ytcp-checkbox-lit/div/div[1]/div/div')
opt2.click()

opt3 = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[5]/div[2]/div[2]/ytcp-form-textarea/div/textarea')
opt3.click()

time.sleep(5)

signature = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/tp-yt-paper-dialog-scrollable/div/div/div[5]/div[2]/div[2]/ytcp-form-textarea/div/textarea')
signature.send_keys("xxx")

time.sleep(5)

submit = driver.find_element(By.XPATH, '/html/body/ytcr-unified-form/ytcp-modal-dialog/tp-yt-paper-dialog/div/div/div[2]/div[2]/ytcp-button/div')
submit.click()

time.sleep(1000)
