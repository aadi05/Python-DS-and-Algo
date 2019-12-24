from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="A:/chromedriver/chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
messages = "Blackboard"

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

while True:
	time.sleep(15)
	for msg in messages:
		msg_box.send_keys(msg)
		button = driver.find_element_by_class_name('_3M-N-')
		button.click()