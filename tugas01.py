from selenium import webdriver

driver = webdriver.Chrome()
driver.minimize_window()
driver.implicitly_wait(10)


url_list = ('https://noobtest.id/', 'https://erzaf.com/', 'https://www.orangsiber.com/', 'http://automatetheboringstuff.com/')

for url in url_list:
    driver.get(url)
    print(driver.current_url, ' - ' , driver.title)

driver.close()
