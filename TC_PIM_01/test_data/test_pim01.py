from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Data import data
from Locators import locators


class Test_OrangeHRM:


   @pytest.fixture
   def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.implicitly_wait(10)
       yield
       self.driver.close()


   def test_login(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
       self.driver.implicitly_wait(10)
       assert self.driver.current_url == data.Web_Data().dashboard_url
       print("SUCCESS : Logged in with Username {a} & Password {b}".format(a=data.Web_Data().username, b=data.Web_Data.password))


   def add_employee(self, booting_function):
       self.driver.find_element(by=By.LINK_TEXT, value=locators.Web_Locators().pim_locator).click()
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().add_button_locator).click()
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().employee_firstname_locator).send_keys(data.Web_Data().employee_first_name)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().employee_lastname_locator).send_keys(data.Web_Data().employee_last_name)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().employee_id_locator).clear()
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().employee_id_locator).send_keys(data.Web_Data().employee_id)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().save_button_locator).click()
       assert self.driver.current_url != data.Web_Data().dashboard_url
       print("Employee details saved successfully.")