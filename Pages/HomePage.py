
import logging

from Pages.BasePage import BaseFather
from Pages.NewCarPage import NewCarPage
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)

class HomePage(BaseFather):

    def __init__(self,mydriver):
        super().__init__(mydriver)

    def go_to_new_car(self):
        self.mousehover("new_car_xpath")
        self.click("find_new_car_xpath")
        return NewCarPage(self.driver)
