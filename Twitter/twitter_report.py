from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://help.twitter.com/en/forms/ipi/dmca/authorized-rep")

time.sleep(2)

burger=driver.find_element(By.XPATH, '/html/body/div/div[5]/div/div/div/div/div[2]/div/div[1]/button/div')
burger.click()

time.sleep(4)

sign_in=driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/a')
sign_in.click()

time.sleep(3)

email=driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
email.send_keys("vinnie.kolt@marsoak.com")

time.sleep(3)

next_button=driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
next_button.click()

time.sleep(5)

password=driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys("random1$A")

time.sleep(5)

log_in=driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
log_in.click()

time.sleep(3)

#captcha
Authenticate_button=driver.find_element(By.XPATH, '//*[@id="triggerLiteMode"]')
Authenticate_button.click()

time.sleep(10)


copy_owner_full_name = driver.find_element(By.XPATH ,'/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/input')
copy_owner_full_name.send_keys("Marcelle Haddad")

time.sleep(2)

full_name = driver.find_element(By.XPATH ,'/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/input')
full_name.send_keys("Emilio Dandan")

time.sleep(2)

company = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[2]/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/input')
company.send_keys("UL")

time.sleep(2)

job_title = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[2]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]/input')
job_title.send_keys("Srudent")

time.sleep(3)


street_address = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[2]/div[1]/div/div/div[2]/div[7]/div[1]/div[2]/input')
street_address.send_keys("Fanar")

time.sleep(4)

city = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[2]/div[1]/div/div/div[2]/div[8]/div[1]/div[2]/input')
city.send_keys("Fanar")

time.sleep(4)

country_select = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[2]/div[1]/div/div/div[2]/div[11]/div[1]/fieldset/select')
country_select.click()

time.sleep(2)

leb = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[2]/div[1]/div/div/div[2]/div[11]/div[1]/fieldset/select/option[123]')
leb.click()

time.sleep(4)

twitter_opt = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div/span/input')
twitter_opt.click()

time.sleep(4)

photo_opt = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[4]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/span/input')
photo_opt.click()

time.sleep(5)

desc_work = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[4]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/textarea')
desc_work.send_keys("This account stole my content!")

time.sleep(5)

link_work = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[4]/div[1]/div/div/div[2]/div[3]/div[1]/ul/li/div/div[3]/input')
link_work.send_keys("https://x.com/oIdnewera/status/1772494930998383056?s=20")

time.sleep(5)

infringing_url = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[5]/div[1]/div/div/div[2]/div[1]/div[1]/ul/li/div/div[3]/input')
infringing_url.send_keys("https://x.com/forsainz/status/1772339847338016963?s=20")

time.sleep(5)

desc_infri = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[5]/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/textarea')
desc_infri.send_keys("This account posted my photo without my permission")

time.sleep(4)

opt_1 = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[6]/div[1]/div[2]/div[1]/div[2]/div/div/div/span/input')
opt_1.click()

time.sleep(1)

opt_2 = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[6]/div[1]/div[3]/div[1]/div[2]/div/div/div/span/input')
opt_2.click()

time.sleep(1)

opt_3 = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[6]/div[1]/div[4]/div[1]/div[2]/div/div/div/span/input')
opt_3.click()

time.sleep(1)

signature = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[6]/div[1]/div[7]/div[1]/div[2]/input')
signature.send_keys("Emilio Dandan")

time.sleep(5)

send_btn = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[8]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[5]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/form/div/div[6]/div[1]/div[19]/button')
send_btn.click()