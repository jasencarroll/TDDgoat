from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"

browser = webdriver.Firefox(options=options)
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title