import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self,host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit = True)

    def get_group_list(self):
        group_list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, email from addressbook")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, email1) = row
                contact_list.append(Contact(id=str(id), first_name=firstname, last_name=lastname,
                                            home_phone=home, mobile_phone=mobile, work_phone=work,
                                            email1=email1))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()