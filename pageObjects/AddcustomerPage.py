from selenium.webdriver.support.ui import Select

import time

class AddCustomer():
    lnkCustomers_menu_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/a"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdGenderMale_id = "Gender_Male"
    rdGenderFemale_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lsitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lsitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lsitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lsitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lsitemVendors_xpath = " //li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lsitemRegistered_xpath)
        elif role == "Administartors":
            self.listitem = self.driver.find_element_by_xpath(self.lsitemAdministrators_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lsitemGuests_xpath)
        elif role == "Registered":
            self.listitem = self.listitem = self.driver.find_element_by_xpath(self.lsitemRegistered_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element_by_xpath(self.sitemForumModerators_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lsitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lsitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click() this should work sometimes, but if click method is not working , we use java script below
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdGenderMale_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdGenderFemale_id).click()
        else:
            self.driver.find_element_by_id(self.rdGenderMale_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
    
