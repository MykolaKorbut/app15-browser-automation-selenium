import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebAutomation:
    def __init__(self):
        # Define driver, options, and service
        chrome_options = Options()
        chrome_options.add_argument('--disable-search-engine-choice-screen')

        download_path = os.getcwd()
        prefs = {"download.default_directory": download_path}
        chrome_options.add_experimental_option("prefs", prefs)

        service = Service('chromedriver-mac-arm64/chromedriver')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Load the webpage
        self.driver.get('https://demoqa.com/login')

        # Locate username, password, and login button
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in username and password, and click the button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, full_name, email, current_address, permanent_address):
        # Locate the Elements dropdown and Text Box
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form field and submit button
        fullname_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form field
        fullname_field.send_keys(full_name)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Scroll to make the element visible and locate the Upload and Download section and the Download button
        upload_download = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'item-7')))
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   upload_download)
        upload_download.click()
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    web_automation = WebAutomation()
    web_automation.login('pythonstudent', 'PythonStudent123$')
    web_automation.fill_form('John Smith', 'Smith@python.com', 'USA', 'USA')
    web_automation.download()
    web_automation.close()