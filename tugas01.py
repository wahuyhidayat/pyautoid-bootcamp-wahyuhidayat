from selenium import webdriver

driver = webdriver.Chrome()
driver.minimize_window()
driver.implicitly_wait(10)


url_list = ('https://noobtest.id/', 'https://erzaf.com/', 'https://www.orangsiber.com/', 'http://automatetheboringstuff.com/')

for url in url_list:
    driver.get(url)
    current_url = driver.current_url
    delims = ['//', '/']
    for d in delims:
        current_url = current_url.replace(d, '-')
    print(current_url.split('-')[1], ' - ' , driver.title)

driver.close()
