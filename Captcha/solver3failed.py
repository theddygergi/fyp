from selenium import webdriver
from selenium.webdriver.common.by import By
from capmonster_python import RecaptchaV2Task
from time import sleep


class RecaptchaV2Selenium:
    def __init__(self, _client_key):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        self.captcha = RecaptchaV2Task(_client_key)
        self.browser = webdriver.Firefox()
        self.website_url = "https://www.google.com/recaptcha/api2/demo"

    def _get_site_key(self):
        self.browser.get("https://www.google.com/recaptcha/api2/demo")
        return self.browser.find_element(By.ID, "recaptcha-demo").get_attribute("data-sitekey")

    def _solve_recaptcha(self):
        self.captcha.set_user_agent(self.user_agent)
        task_id = self.captcha.create_task(website_url=self.website_url,
                                           website_key=self._get_site_key(),
                                           no_cache=True)
        return self.captcha.join_task_result(task_id=task_id, maximum_time=180).get("gRecaptchaResponse")

    def submit_form(self):
        self.browser.execute_script("document.getElementsByClassName('g-recaptcha-response')[0].innerHTML = "
                                    f"'{self._solve_recaptcha()}';")
        self.browser.find_element(By.ID,"recaptcha-demo-submit").click()
        sleep(10)
        self.browser.close()
        return self.browser.find_element(By.CLASS_NAME,"recaptcha-success")


if __name__ == "__main__":
    client_key = "b5eb1c1ef3a677895c9728cf56758b81"
    executable_path = "exepath"
    recaptcha_selenium = RecaptchaV2Selenium(client_key)