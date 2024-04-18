from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import out_op as op
import random as rd

def rand_time():
    return rd.randint(2,6)

driver = webdriver.Firefox()
driver.get('https://support.github.com/contact/trademark-policy')

sign_in_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/header/div[2]/a[1]')
sign_in_btn.click()

sleep(rand_time())

email = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[3]/form/input[2]')
email.send_keys("marcelle.haddad@outlook.com")

sleep(rand_time())

password = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[1]')
password.send_keys("marcelle1q2w3e4r5t")

sleep(rand_time())


sign_in_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[13]')
sign_in_btn.click()

sleep(rand_time())


trademark_holder_opt = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/dl[2]/dd[1]/select')
trademark_holder_opt.click()

sleep(rand_time())


i_am_trademark_owner_opt = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/dl[2]/dd[1]/select/option[2]')
i_am_trademark_owner_opt.click()

sleep(rand_time())


registred_trd_opt = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[1]/dd[1]/select')
registred_trd_opt.click()

sleep(rand_time())


no_reg_trd_opt = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[1]/dd[1]/select/option[3]')
no_reg_trd_opt.click()

sleep(rand_time())


name = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/div[2]/dl[1]/dd[1]/input')
name.send_keys("Marcelle Haddad")

sleep(rand_time())


company_email = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/div[2]/dl[4]/dd[1]/input')
company_email.send_keys("marcelle.haddad@outlook.com")

sleep(rand_time())


contact_address = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/div[2]/dl[5]/dd[1]/textarea')
contact_address.send_keys("Georgia")

sleep(rand_time())


revised_trd_opt = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[2]/dd[1]/select')
revised_trd_opt.click()

sleep(rand_time())

no_opt = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[2]/dd[1]/select/option[3]')
no_opt.click()

sleep(rand_time())

urls_to_report = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[4]/dd[1]/textarea')
urls_to_report.send_keys("https://github.com/marcellehaddad/myfitnessandroid")

sleep(rand_time())

report_desc = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[5]/dd[1]/textarea')
report_desc.send_keys("This account stole my repository without asking for my permission. Please consider this reprort.")

sleep(rand_time())

changes_to_removal = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[6]/dd[1]/textarea')
changes_to_removal.send_keys("If the account can ask for permission next time before taking my repository.")

sleep(rand_time())

company_name_trd_holder = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[7]/dd[1]/input')
company_name_trd_holder.send_keys("UL")

sleep(rand_time())

company_website_trd_holder = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[8]/dd[1]/input')
company_website_trd_holder.send_keys("www.ul.com")

sleep(rand_time())

company_github_acc = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[9]/dd[1]/select')
company_github_acc.click()

sleep(rand_time())

not_applicable = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[9]/dd[1]/select/option[2]')
not_applicable.click()

sleep(rand_time())

opt1 = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/div[3]/input[2]')
opt1.click()

sleep(rand_time())

opt2 = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/div[4]/input[2]')
opt2.click()

sleep(rand_time())

opt3 = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/div[5]/input[2]')
opt3.click()

sleep(4)

full_name = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[1]/dl[10]/dd[1]/input')
full_name.send_keys("Marcelle Haddad")

sleep(rand_time())

send_btn = driver.find_element(By.XPATH, '/html/body/main/restorable-form/trademark-policy/form/div[2]/button')
send_btn.click()
