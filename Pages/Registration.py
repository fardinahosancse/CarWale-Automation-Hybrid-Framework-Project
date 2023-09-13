from Pages.BasePage import BaseFather


class Registration(BaseFather):
    def __init__(self,driver):
        super().__init__(driver)

    def fill_form(self,name,phone,email,country,city,username,password):
        self.type("name_xpath",name)
        self.type("phone_xpath",phone)
        self.type("email_xpath",email)
        self.select("country_xpath",country)
        self.type("city_xpath",city)
        self.type("username_xpath",username)
        self.type("password_xpath",password)
        self.click("submit_xpath")
