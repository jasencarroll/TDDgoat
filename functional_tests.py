from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
#options = Options()
#options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"
options = webdriver.ChromeOptions()
options.page_load_strategy = 'none'
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
#browser = webdriver.Firefox(options=options)
browser.get('http://127.0.0.1:8000')

#assert 'Django' in browser.title