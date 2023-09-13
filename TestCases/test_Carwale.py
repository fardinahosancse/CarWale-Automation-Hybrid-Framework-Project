import time

import pytest


from Pages.CarBasePage import CarBasePage
from Pages.HomePage import HomePage
from TestCases.BaseFatherTest import BaseFatherTest
from Utility import dataProvider

import logging
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)


class Test_CarWale(BaseFatherTest):

    @pytest.mark.parametrize("carBrand,carTitle",dataProvider.get_data("car","../Excel/carwale.xlsx"))
    def test_SelectCar(self,carBrand,carTitle):
        home = HomePage(self.driver)
        car = CarBasePage(self.driver)
        print(carBrand)
        if carBrand == "Maruti":
            home.go_to_new_car().goTo_maruti()
            title=car.get_title()
            print("Car Title is : ",title)
            assert title == carTitle ,"MisMatched"
            car.get_price_name()
        elif carBrand == "Hyundai":
            home.go_to_new_car().goTo_hynudai()
            title = car.get_title()
            print("Car Title is : ", title)
            assert title == carTitle, "MisMatched"
            car.get_price_name()
        elif carBrand == "Tata":
            home.go_to_new_car().goTo_tata()
            title = car.get_title()
            print("Car Title is : ", title)
            assert title == carTitle, "MisMatched"
            car.get_price_name()
        elif carBrand == "Toyota":
            home.go_to_new_car().goTo_toyota()
            title = car.get_title()
            print("Car Title is : ", title)
            assert title == carTitle, "MisMatched"
            car.get_price_name()
        elif carBrand == "Mahindra":
            home.go_to_new_car().goTo_mahindra()
            title = car.get_title()
            print("Car Title is : ", title)
            assert title == carTitle, "MisMatched"
            car.get_price_name()
        time.sleep(10)



