import pytest
from Pages.Registration import Registration
from TestCases.BaseFatherTest import BaseFatherTest
from Utility.dataProvider import get_data

import logging
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)

class Test_Registration(BaseFatherTest):

    @pytest.mark.skip
    @pytest.mark.parametrize("name,phone,email,country,city,username,password",get_data("LoginTest"))
    def test_doReg(self,name,phone,email,country,city,username,password):
        log.logger.info("Test_Registartion Started")
        #object of Registration Class
        reg = Registration(self.driver)
        reg.fill_form(name,phone,email,country,city,username,password)
        log.logger.info("Test_Registartion Successfully Executed")



