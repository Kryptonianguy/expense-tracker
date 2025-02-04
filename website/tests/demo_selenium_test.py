# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# service = Service(executable_path=r"D:\Projects\expense-tracker\website\tests\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get("http://127.0.0.1:5000/")
# time.sleep(10)
# print(driver.title)
# driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver Manager will automatically install and use the correct ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:5000/")
time.sleep(10)
print(driver.title)
driver.quit()