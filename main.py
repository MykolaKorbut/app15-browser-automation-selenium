from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://demoqa.com/login')

input("Press Enter to quit.")
driver.quit()
