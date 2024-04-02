import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RobotTest:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.file_path = os.path.join("ss.jpg")

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://blueimp.github.io/jQuery-File-Upload/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_robot(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.fileinput-button"))).click()
        self.upload_file_with_robot(self.file_path)
        assert self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".name"))).text == "ss.jpg"
        time.sleep(2)

    def teardown(self):
        self.driver.quit()

    def upload_file_with_robot(self, file_path):
        time.sleep(1)  # Add a small delay to give time for the file dialog to appear
        pyautogui.write(file_path)
        pyautogui.press('enter')

if __name__ == "__main__":
    test = RobotTest()
    test.setup()
    test.test_robot()
    test.teardown()
