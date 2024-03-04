from selenium import webdriver
import subprocess
import time


name = 'LPU Block-34'
ssid = 'LPU Block-34'

# subprocess.run(['netsh', 'wlan', 'connect', 'name=',name, 'ssid=',ssid])
# time.sleep(2)

driver = webdriver.Chrome
url = 'https://www.google.com'
driver.get(url)
driver.fullscreen_window()
time.sleep(0.5)

username = driver.find_element('name','username')
password = driver.find_element('name','password')
terms_and_conditions = driver.find_element('id', 'agreepolicy')
login = driver.find_element('id', 'loginbtn')

username.send_keys('12212251')
password.send_keys('Pass@123')
time.sleep(0.3)
terms_and_conditions.click()
time.sleep(0.3)
login.click()

time.sleep(2)
driver.quit()
