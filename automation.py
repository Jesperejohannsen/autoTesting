from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


chrome_browser = webdriver.Chrome("./chromedriver.exe")

chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name("btn-default")

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys("This is a test")


show_message_button.click()

output_message = chrome_browser.find_element_by_id("display")

assert "This is a test" in output_message.text

chrome_browser.quit()