import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTextBox:

    data_user = [('wahyu', 'wahyu@hidayat.com', 'jakarta', 'indonesia')]

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://demoqa.com/text-box')


    @pytest.mark.parametrize('fullName, email, currentAdd, permanentAdd', data_user)
    def test_text_box(self, fullName, email, currentAdd, permanentAdd):
        self.driver.find_element(By.ID, 'userName').send_keys(fullName)
        self.driver.find_element(By.ID, 'userEmail').send_keys(email)
        self.driver.find_element(By.ID, 'currentAddress').send_keys(currentAdd)
        self.driver.find_element(By.ID, 'permanentAddress').send_keys(permanentAdd)
        self.driver.find_element(By.ID, 'submit').click()

        expected_name = 'Name:'+ f'{fullName}'
        actual_name = self.driver.find_element(By.ID, 'name').text
        assert expected_name == actual_name, f"Error. Expected name is {expected_name}, but actual name is {actual_name}"

        expected_email = 'Email:'+ f'{email}'
        actual_email = self.driver.find_element(By.ID, 'email').text
        assert expected_email == actual_email, f"Error. Expected email is {expected_email}, but actual email is {actual_email}"

        expected_current = 'Current Address :'+ f'{currentAdd}'
        actual_current = self.driver.find_element(By.CSS_SELECTOR, 'p#currentAddress').text
        assert expected_current == actual_current, f"Error. Expected current address is {expected_current}, but actual current address is {actual_current}"

        expected_permanent = 'Permananet Address :'+ f'{permanentAdd}'
        actual_permenent = self.driver.find_element(By.CSS_SELECTOR, 'p#permanentAddress').text
        assert expected_permanent == actual_permenent, f"Error. Expected permenent address is {expected_permanent}, but actual permenent address is {actual_permenent}"

    def teardown(self):
        self.driver.quit()
