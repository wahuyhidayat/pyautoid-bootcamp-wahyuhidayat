from selenium import webdriver
from selenium.webdriver.common.by import By
import time


data_list = [
    ('John','Snow','john@snow.com', 29, 2900000, 'Dark Knight'),
    ('Arya','Stark','arya@stark.com', 19, 1900000, 'King Slayer'),
    ('Sansa','Stark','sansa@stark.com', 25, 2500000, 'Princess')
]


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/webtables")

for data in data_list:
    add_button = driver.find_element(By.ID, "addNewRecordButton")
    add_button.click()

    driver.find_element(By.ID, "firstName").send_keys(data[0])
    driver.find_element(By.ID, "lastName").send_keys(data[1])
    driver.find_element(By.ID, "userEmail").send_keys(data[2])
    driver.find_element(By.ID, "age").send_keys(data[3])
    driver.find_element(By.ID, "salary").send_keys(data[4])
    driver.find_element(By.ID, "department").send_keys(data[5])
    driver.find_element(By.ID, "submit").click()

time.sleep(5)
driver.close()
