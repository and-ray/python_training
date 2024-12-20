from time import sleep
from selenium.webdriver.common.by import By
from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def edit_contact(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("address", contact.address)

    def fill_first_contact_with_group(self, contact, group):
        wd = self.app.wd
        self.edit_contact(contact)
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(group.name)

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
        self.edit_contact(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_list_cache = None

    def create_with_group(self, contact, group):
        wd = self.app.wd
        self.open_contact_creation_page()
        self.fill_first_contact_with_group(contact, group)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_list_cache = None

    def open_contact_creation_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("firstname")) >0 and len(wd.find_elements_by_name("middlename"))>0 and
                len(wd.find_elements_by_name("lastname"))>0 and len(wd.find_elements_by_name("submit")) ==2 ):
            sleep(5) # CONTACT TESTS DO NOT WORK WITHOUT THIS SLOW BUTTON
            wd.find_element_by_link_text("add new").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        # select
        wd.find_elements_by_name("selected[]")[index].click()
        # exterminate
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.return_to_home_page()
        self.contact_list_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(id)
        # exterminate
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.return_to_home_page()
        self.contact_list_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//a[@href='edit.php?id=" + id + "']/img[@title='Edit']").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_by_index(self, contact, index):
        wd = self.app.wd
        self.return_to_home_page()
        # select
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index+1].click()
        #edit
        self.edit_contact(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_list_cache = None

    def modify_by_id(self, modify_data, id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(id)
        self.edit_contact(modify_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_list_cache = None

    def modify_first(self, contact):
        self.modify_by_index(contact, 0)

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len (wd.find_elements_by_name("selected[]"))

    contact_list_cache = None

    def get_contact_list(self):
       if self.contact_list_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_list_cache = []
            for each_element in wd.find_elements_by_xpath("//table[@id='maintable']//tr[@name]"):
                last_name = each_element.find_element_by_xpath("td[2]").text
                first_name = each_element.find_element_by_xpath("td[3]").text
                id = str(each_element.find_element_by_xpath("td/input").get_attribute("id"))
                address = each_element.find_element_by_xpath("td[4]").text
                all_emails = each_element.find_element_by_xpath("td[5]").text #.replace(" ", "")
                all_phones = each_element.find_element_by_xpath("td[6]").text.replace(" ", "")
                self.contact_list_cache.append(Contact(last_name=last_name,
                                                       first_name=first_name,
                                                       id=id,
                                                       address=address,
                                                       all_phones_from_home_page=all_phones,
                                                       all_emails_from_home_page = all_emails
                                                       ))
       return list(self.contact_list_cache)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        all_phones_field = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", all_phones_field).group(1)
        mobile_phone = re.search("M: (.*)", all_phones_field).group(1)
        work_phone = re.search("W: (.*)", all_phones_field).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = " ".join(wd.find_element_by_name("home").get_attribute("value").split())
        mobile_phone = " ".join(wd.find_element_by_name("mobile").get_attribute("value").split())
        work_phone = " ".join(wd.find_element_by_name("work").get_attribute("value").split())
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return(Contact(last_name=last_name, first_name=first_name, id=id, home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone,
                       email=email, email2=email2, email3=email3, address=address))

    def select_contact_to_delete_from_group(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@id='%s']" %contact.id).click()

    def delete_contact_from_group(self):
        wd = self.app.wd
        wd.find_element_by_name("remove").click()

    def add_contact_to_group(self, contact, group_name):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[contains(@title,'%s')]" %contact.first_name).click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group_name)
        wd.find_element_by_xpath("//input[@name='add']").click()

    def get_id(self, first_name):
        wd = self.app.wd
        return wd.find_element_by_xpath("//input[contains(@title,'%s')]" % first_name).get_attribute("value")



def clear_phone(phone):
    return re.sub("[() -]","", phone)

def  merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear_phone(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.home_phone,
                                                           contact.mobile_phone,
                                                           contact.work_phone])))).replace(" ", "")


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  filter(lambda x: x is not None,[contact.email, contact.email2, contact.email3])))