from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://demoqa.com/alerts')

driver.find_element_by_id('timerAlertButton').click()

try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print('alert has been clicked.')
except TimeoutException:
    print('alert not found.')
    pass

driver.close()
