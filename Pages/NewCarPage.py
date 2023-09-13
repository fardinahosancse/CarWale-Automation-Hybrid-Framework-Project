import logging

from Pages.BasePage import BaseFather
from Utility.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class NewCarPage(BaseFather):
    def __init__(self,driver):
        super().__init__(driver)

    def goTo_maruti(self):
        self.click("maruti_xpath")

    def goTo_hynudai(self):
        self.click("hyundai_xpath")

    def goTo_toyota(self):
        self.click("toyota_xpath")

    def goTo_tata(self):
        self.click("tata_xpath")

    def goTo_mahindra(self):
        self.click("mahindra_xpath")

    def goTo_bmw(self):
        self.click("bmw_xpath")

    def goTo_porshe(self):
        self.click("porshe_xpath")

    def goTo_kia(self):
        self.click("kia_xpath")

    def goTo_marchedes(self):
        self.click("marcedes_xpath")

    def goTo_mg(self):
        self.click("mg_xpath")

    def goTo_honda(self):
        self.click("honda_xpath")

    def goTo_landrover(self):
        self.click("landrover_xpath")



