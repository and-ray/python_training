from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_first_contact(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("email", contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.app.return_to_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


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

