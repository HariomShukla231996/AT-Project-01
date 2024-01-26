from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException




class Hariom:
   driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


   def start(self):
       self.driver.maximize_window()
       self.driver.get(data.Web_Data().url)
       self.driver.implicitly_wait(10)


   def employee_data_delete(self):
       try:
           self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
           self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
           self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
           self.driver.implicitly_wait(6)
           self.driver.find_element(by=By.LINK_TEXT, value=locators.Web_Locators().pim_locator).click()
           self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().delete_button_locator).click()
           self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().sure_to_delete_locator).click()
       except NoSuchElementException as e:
           print("Error : ", e)
       finally:
           self.driver.quit()
           print("Employee Data Deleted Successfully")


if __name__ == '__main__':
   hari = Hariom()
   hari.start()
   hari.employee_data_delete()

