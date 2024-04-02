from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui



driver = webdriver.Firefox()
driver.get('https://www.tiktok.com/legal/report/Copyright')



email = driver.find_element(By.CSS_SELECTOR, '#tux-70191_input') # er b tiktok 💗
email.send_keys('bahsa.leb@gmail.com')

#email = driver.find_element(By.CSS_SELECTOR, '#tux-61912_input')
#email.send_keys('bahsa.leb@gmail.com')


time.sleep(5)

next_btn = driver.find_element(By.CSS_SELECTOR , 'body > div.base-layout-container > main > article > div > form > button')
next_btn.click()

time.sleep(2)


#done_btn = driver.find_element(By.CSS_SELECTOR, 'button.submit-button:nth-child(5)')
#done_btn.click()
WebDriverWait(driver , 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'css-1mu1jn5'))
)

problem_selection = driver.find_element(By.CLASS_NAME , 'css-1mu1jn5')
problem_selection.click()

time.sleep(5)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located ((By.CLASS_NAME , 'css-1o2kt1p'))
)


subproblem_selection = driver.find_element(By.CLASS_NAME, 'css-1o2kt1p')
subproblem_selection.click()

time.sleep(5)

affected = driver.find_element(By.XPATH, '//*[@id="tux-4_button"]')
affected.click()

time.sleep(4)
WebDriverWait(driver , 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="tux-4_list_1"]'))
)

affected_select = driver.find_element(By.XPATH, '//*[@id="tux-4_list_1"]')
affected_select.click()

time.sleep(4)


full_name = driver.find_element(By.XPATH, '//*[@id="tux-6_input"]')
full_name.send_keys("Bahsa Leb")

time.sleep(5)

copyright_owner_name = driver.find_element(By.XPATH, '//*[@id="tux-7_input"]')
copyright_owner_name.send_keys("Edz")

time.sleep(4)

physical_address = driver.find_element(By.XPATH , '//*[@id="tux-8_input"]')
physical_address.send_keys("Georgia")

time.sleep(4)

phone_nb = driver.find_element(By.XPATH, '//*[@id="tux-9_input"]')
phone_nb.send_keys("+995577208104")

time.sleep(5)

option = driver.find_element(By.XPATH, '//*[@id="Photo / Picture"]')
option.click()

time.sleep(2)

copyright_src = driver.find_element(By.XPATH , '//*[@id="My personal TikTok account"]')
copyright_src.click()

time.sleep(4)

url_text1 = driver.find_element(By.XPATH , '//*[@id="tux-26_input"]')
url_text1.send_keys("https://vt.tiktok.com/ZSFUArf2c/")

time.sleep(4)

url_text2 = driver.find_element(By.XPATH , '//*[@id="tux-27_textArea"]')
url_text2.send_keys("https://vt.tiktok.com/ZSFUArf2c/")

time.sleep(4)

desc_text = driver.find_element(By.XPATH , '//*[@id="tux-28_input"]')
desc_text.send_keys("This person stole my content without my permission ya haywen!! 🐎")

time.sleep(5)

#try:
upload_btn = driver.find_element(By.XPATH, '//*[@id="input-file-authorizations"]')
pyautogui.write("ss.jpg")
pyautogui.press('enter')

#except :
    #pass



time.sleep(4)

url_text3 = driver.find_element(By.XPATH , '//*[@id="tux-20_textArea"]')
url_text3.send_keys("https://vt.tiktok.com/ZSFUArf2c/")

time.sleep(5)


#prevent_btn = driver.find_element(By.XPATH, '/html/body/div[3]/main/form/div[16]/div/div/div/input')
#prevent_btn.click()

time.sleep(5)

first_opt = driver.find_element(By.XPATH, '/html/body/div[3]/main/form/div[23]/div/div[1]/div')
first_opt.click()

time.sleep(5)

second_opt = driver.find_element(By.XPATH, '/html/body/div[3]/main/form/div[23]/div/div[2]/div')
second_opt.click()

time.sleep(5)

third_opt = driver.find_element(By.CSS_SELECTOR, 'div.css-ypesld:nth-child(3) > div:nth-child(2)')
third_opt.click()

time.sleep(5)

signature = driver.find_element(By.ID , 'tux-25_input')
signature.send_keys("Bahsa Leb")

time.sleep(5)

send_btn = driver.find_element(By.XPATH, '/html/body/div[3]/main/form/button')
send_btn.click()

time.sleep(100)

