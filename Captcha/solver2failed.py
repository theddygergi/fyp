import undetected_chromedriver as uc
from twocaptcha import TwoCaptcha
from selenium.webdriver.common.by import By
import time

#not working 
def solve_captcha(web):
    driver = uc.Chrome()
    driver.get(web)

    # Get site key
    sitekey = driver.find_element(By.ID, value='recaptcha-demo').get_attribute('data-sitekey')
    print(f"Site Key: {sitekey}")

    api_key = "b5eb1c1ef3a677895c9728cf56758b81"
    solver = TwoCaptcha(api_key)
    print("Solving captcha...")
    response = solver.solve_captcha(sitekey=sitekey, url=web)

    print(f'Captcha Key: {response["code"]}')

    # Send Captcha Key to form
    driver.execute_script("document.getElementById('g-recaptcha-response').value = '{}';".format(response["code"]))

    # Click Submit
    driver.find_element(By.XPATH,value='//*[@id="recaptcha-demo-submit"]').click()

    time.sleep(5)

# Usage example
web = input("Enter URL: ")
solve_captcha(web)