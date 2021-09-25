from selenium import webdriver
from selenium.webdriver.common.by import By
import time

data_dict = [
    {'firstName': 'John', 'lastName':'Snow', 'userEmail':'john@snow.com', 'age':'29', 'salary':'2900000', 'department':'Dark Knight'},
    {'firstName': 'Arya', 'lastName':'Stark', 'userEmail':'arya@stark.com', 'age':'19', 'salary':'1900000', 'department':'King Slayer'},
    {'firstName': 'Sansa', 'lastName':'Stark', 'userEmail':'sansa@stark.com', 'age':'25', 'salary':'2500000', 'department':'Princess'}
    ]

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/webtables")

for data in data_dict:
    driver.find_element(By.ID, "addNewRecordButton").click()
    for key in data:
        driver.find_element(By.ID, key).send_keys(data[key])
    driver.find_element(By.ID, "submit").click()

time.sleep(5)
driver.close()
