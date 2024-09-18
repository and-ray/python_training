from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # go back  to groups
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) >0):
            wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        self.select_group_by_index(0)


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #exterminate
        wd.find_element_by_name("delete").click()
        # go back  to groups
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
       self.delete_group_by_index(0)

    def modify_first(self, group):
        self.modify_by_index(group, 0)

    def modify_by_index(self, group, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group modification
        wd.find_element_by_name("update").click()
        # go back  to groups
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len (wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list (self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for each_element in wd.find_elements_by_css_selector("span.group"):
                text = each_element.text
                id = each_element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name = text, id = id))
        return list(self.group_cache)
