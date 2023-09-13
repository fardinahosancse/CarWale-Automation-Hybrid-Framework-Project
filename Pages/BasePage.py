from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utility import configReader as conf
import logging
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)
from selenium.webdriver import ActionChains

class BaseFather:
    def __init__(self,driver):
        self.driver = driver

    def click(self,syntex):
        if str(syntex).endswith("_xpath"):
            self.driver.find_element(By.XPATH,conf.readConfig("locatorsData",syntex)).click()
        log.logger.info(">Clicking on a Element: " + str(syntex))
    def type(self,syntex,syntex_value):
        if str(syntex).endswith("_xpath"):
            self.driver.find_element(By.XPATH,conf.readConfig("locatorsData",syntex)).send_keys(syntex_value)
        log.logger.info(">Typing on Input: " + str(syntex) + "," +str(syntex_value))
    def select(self,syntex,selection_value):
        if str(syntex).endswith("_xpath"):
            Select(self.driver.find_element(By.XPATH,conf.readConfig("locatorsData",syntex))).select_by_value(selection_value)
        log.logger.info(">Selecting : " + str(syntex) + "," + str(selection_value))

    def mousehover(self,syntex):
        configLoader = conf.readConfig("locatorsData",syntex)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,configLoader)).perform()
        log.logger.info(">Mouse Hover : " + str(syntex))


