from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import out_op as op
 
driver = webdriver.Firefox()
driver.get("https://help.instagram.com/contact/552695131608132")
 
option_1 = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[2]/div[3]/label[1]/span')
option_1.click()
 
time.sleep(5)
 
full_name = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[5]/input')
full_name.send_keys("Marcelle Haddad")
 
time.sleep(4)
 
email_address = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[7]/input')
email_address.send_keys("michael.me2@hotmail.com")
 
time.sleep(5)
 
email_address_conf = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[8]/input')
email_address_conf.send_keys("michael.me2@hotmail.com")
 
time.sleep(5)
 
name_rights_owner = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[10]/input')
name_rights_owner.send_keys("Marcelle Hanna")
 
time.sleep(5)
 
select_country = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[11]/select')
select_country.click()
 
time.sleep(4)
 
leb_select = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[11]/select/option[122]')
leb_select.click()
 
time.sleep(3)
 
describe_select = driver.find_element(By.XPATH , '/html/body/div/div/div[3]/div/div[2]/div/form/div[12]/select')
describe_select.click()
 
time.sleep(4)
 
photo_opt = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[12]/select/option[2]')
photo_opt.click()
 
time.sleep(5)
 
url1 = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[13]/textarea')
url1.send_keys("https://www.instagram.com/p/C3mtXDoMWjgnzWKjQ_mGO-iF7ix-RRTEsclRUY0/?igsh=MzRlODBiNWFlZA==")
 
time.sleep(5)
 
photo_opt_2 = driver.find_element(By.XPATH, '//*[@id="1076937109041279.0"]')
photo_opt_2.click()
 
time.sleep(5)
 
url2 = driver.find_element(By.XPATH, '//*[@id="388149281267730"]')
url2.send_keys("https://www.instagram.com/p/C3mtXDoMWjgnzWKjQ_mGO-iF7ix-RRTEsclRUY0/?igsh=MzRlODBiNWFlZA==")
 
time.sleep(5)
 
why_report = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[25]/select')
why_report.click()
 
time.sleep(4)
 
why_report_2 = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[25]/select/option[2]')
why_report_2.click()
 
time.sleep(5)
 
desc = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/div[28]/textarea')
desc.send_keys("This guy posted my picture without my permission. Please consider this report")
 
time.sleep(5)
 
signature = driver.find_element(By.XPATH , '/html/body/div/div/div[3]/div/div[2]/div/form/div[32]/input')
signature.send_keys("Marcella Haddad")
 
send_btn = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/form/button')
send_btn.click()

input_otp = driver.find_element(By.CLASS_NAME, 'inputtext')

otp_code = op.get_outlook_otp("michael.me2@hotmail.com", "random1$A")

time.sleep(4)

input_otp.send_keys(otp_code)

confirm_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[3]/button')
confirm_btn.click()



