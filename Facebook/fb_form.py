from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc
import out_op
 
driver = uc.Chrome()
driver.get("https://facebook.com")
driver.delete_all_cookies()
 
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
 
btn_copy = driver.find_element(By.XPATH, '//*[@id="SupportFormRow.250116565117827"]/div[3]/label[1]/span')
btn_copy.click()
 
time.sleep(2)
 
conf_email = driver.find_element(By.XPATH, '//*[@id="755605467935533"]')
conf_email.send_keys("marcelle.haddad@outlook.com")
 
time.sleep(4)
 
countries = driver.find_element(By.XPATH, '//*[@id="645486236964608"]')
countries.click()
 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[12]/select/option[121]'))
)
 
leb_country = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[12]/select/option[121]')
leb_country.click()
 
time.sleep(3)
 
category = driver.find_element(By.XPATH, '//*[@id="418475341579315"]')
category.click()
 
time.sleep(3)
 
 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[13]/select/option[2]'))
)
 
photo_opt = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[13]/select/option[2]')
photo_opt.click()
 
time.sleep(2)
 
name_copy = driver.find_element(By.XPATH, '//*[@id="1467491100178767"]')
name_copy.send_keys("Emilio Dandan")
 
time.sleep(3)
 
photo_click = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[15]/div[2]/label[1]/span')
photo_click.click()
 
time.sleep(2)
 
photo_url = driver.find_element(By.XPATH, '//*[@id="173734026110493"]')
photo_url.send_keys("https://www.facebook.com/photo/?fbid=122102856158249533&set=a.1221028562062495334")
 
time.sleep(4)
 
photo_url2 = driver.find_element(By.XPATH, '//*[@id="388149281267730"]')
photo_url2.send_keys("https://www.facebook.com/photo/?fbid=122102856158249533&set=a.1221028562062495334")
 
time.sleep(4)
 
reason = driver.find_element(By.XPATH, '//*[@id="136284146523176"]')
reason.click()
 
time.sleep(4)
 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[27]/select/option[2]'))
)
 
copies_work = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[2]/div/div[2]/div[27]/select/option[2]')
copies_work.click()
 
time.sleep(4)
 
add_info = driver.find_element(By.XPATH , '//*[@id="451242651624945"]')
add_info.send_keys("The facebook account Michael Merri posted one of my profile pictures to his facebook feed without asking my permission. Please consider this report")
 
time.sleep(6)
 
ele_signature = driver.find_element(By.XPATH , '//*[@id="159694930852744"]')
ele_signature.send_keys("Marcelle Haddad")
 
submit_btn = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/form/div/div[3]/div/button')
submit_btn.click()
 
time.sleep(10)
 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[2]/div[2]/div/input'))
)
#bypass captcha and otp
input_otp=driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[2]/div[2]/div/input")
time.sleep(10)
OTP_code = out_op.get_outlook_otp("marcelle.haddad@outlook.com", "marcelle1q2w3e4r5t")
time.sleep(10)
input_otp.send_keys(OTP_code)
 
confirm_button=driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[3]/button")
confirm_button.click()
 
time.sleep(10)

"""WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]'))
)"""


recaptcha_checkbox=driver.find_element(By.CLASS_NAME, 'g-recaptcha')

recaptcha_checkbox.click()
time.sleep(300)