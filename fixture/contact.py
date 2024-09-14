from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.app.return_to_home_page()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_first_contact(contact)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select
        wd.find_element_by_name("selected[]").click()
        # exterminate
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.app.return_to_home_page()

    def modify_first(self, contact):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select
        wd.find_element(By.XPATH, "//img[@title='Edit']").click()
        #edit
        self.fill_first_contact(contact)


