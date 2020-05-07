from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.GetApplicationURL()
    username = ReadConfig.GetUseremail()
    password = ReadConfig.GetPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*************** Test_001_Login ******************")
        self.logger.info("***** Started Home Page title test ******")
        self.driver = setup
        self.logger.info("***** Open URL ******")
        self.driver.get(self.baseURL)
        act_title = self.driver.title


        if act_title == "Your store. Login":
            self.logger.info("***** Home page title passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Home page title failed ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("***** Started Login test ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("***** Login test passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Started Login failed ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
            
