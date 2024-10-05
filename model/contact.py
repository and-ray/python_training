from sys import maxsize

class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, id=None, address=None,
                 email1=None,  email2=None,  email3=None,
                 home_phone=None,mobile_phone = None, work_phone = None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None): #, secondary_phone = None
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.id = id

    def __repr__(self):
        return ("id=%s, first_name=%s, middle_name=%s, last_name=%s,  home_phone=%s, mobile_phone=%s, work_phone=%s, "
                "email1=%s, email2=%s, email3=%s, address=%s"
               #, "all_phones_from_home_page%s, all_emails_from_home_page%s"
                ) %(self.id, self.first_name,  self.middle_name, self.last_name,
                                                                              self.home_phone, self.mobile_phone, self.work_phone,
                                                                              self.email1, self.email2, self.email3, self.address,
                                                                           #   self.all_phones_from_home_page, self.all_emails_from_home_page
                    )

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize