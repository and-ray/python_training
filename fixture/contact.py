from time import sleep
from selenium.webdriver.common.by import By
from model.contact import Contact

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


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) >0):
            wd.find_element_by_link_text("home").click()


    def create(self, contact):
        wd = self.app.wd
        self.open_contact_creation_page()
        self.fill_first_contact(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def open_contact_creation_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("firstname")) >0 and len(wd.find_elements_by_name("middlename"))>0 and len(wd.find_elements_by_name("lastname"))>0 and len(wd.find_elements_by_name("submit")) ==2 ):
            sleep(5) # CONTACT TESTS DO NOT WORK WITHOUT THIS SLOW BUTTON
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        # select
        wd.find_element_by_name("selected[]").click()
        # exterminate
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.return_to_home_page()

    def modify_first(self, contact):
        wd = self.app.wd
        self.return_to_home_page()
        # select
        wd.find_element(By.XPATH, "//img[@title='Edit']").click()
        #edit
        self.fill_first_contact(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len (wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_home_page()
        contact_list = []
        #full_list = wd.find_elements_by_xpath("//table[@id='maintable']//tr[@name]")
        for each_element in  wd.find_elements_by_xpath("//table[@id='maintable']//tr[@name]"):
            last_name = each_element.find_element_by_xpath("td[2]").text
            first_name = each_element.find_element_by_xpath("td[3]").text
            #email = each_element.text
            #home_phone = each_element.text
            id_line = str(each_element.find_element_by_xpath("td[@class]/a").get_attribute("href")) #view.php?id=69
            id = id_line[len(id_line)-2:len(id_line)] #view.php?id=69
            contact_list.append(Contact(last_name=last_name, first_name=first_name, id=id))
        return contact_list