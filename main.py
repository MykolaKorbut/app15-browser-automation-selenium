import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver, options, and service
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

download_path = os.getcwd()
prefs = {"download.default_directory": download_path}
chrome_options.add_experimental_option("prefs", prefs)

service = Service('chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(options=chrome_options, service=service)

# Load the webpage
driver.get('https://demoqa.com/login')

# Locate username, password, and login button
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'userName'))
)
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'password'))
)
login_button = driver.find_element(By.ID, 'login')

# Fill in username and password, and click the button
username_field.send_keys('pythonstudent')
password_field.send_keys('PythonStudent123$')
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elements dropdown and Text Box
elements = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,
                                      '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))
)
elements.click()
text_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'item-0'))
)
text_box.click()

# Locate the form field and submit button
fullname_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'userName'))
)
email_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'userEmail'))
)
current_address_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'currentAddress'))
)
permanent_address_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'permanentAddress'))
)
submit_button = driver.find_element(By.ID, 'submit')

# Fill in the form field
fullname_field.send_keys('John Smith')
email_field.send_keys('smith@python.com')
current_address_field.send_keys('USA')
permanent_address_field.send_keys('USA')
driver.execute_script("arguments[0].click();", submit_button)

# Scroll to make the element visible and locate the Upload and Download section and the Download button
upload_download = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'item-7'))
)
driver.execute_script("arguments[0].scrollIntoView();", upload_download)
upload_download.click()
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)

input("Press Enter to quit.")
driver.quit()