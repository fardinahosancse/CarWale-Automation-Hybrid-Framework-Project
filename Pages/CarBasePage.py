from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BaseFather
from Utility import configReader
import logging
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)

class CarBasePage:
    def __init__(self,driver):
        self.mydriver = driver

    def get_title(self):
        return self.mydriver.find_element(By.XPATH, configReader.readConfig("locatorsData", "car_title")).text

    def get_price_name(self):
        carNames = self.mydriver.find_elements(By.XPATH,configReader.readConfig("locatorsData","car_name"))
        carPrices = self.mydriver.find_elements(By.XPATH,configReader.readConfig("locatorsData","car_price"))
        for i in range(1,len(carPrices)):
            print(carNames[i].text,carPrices[i].text)