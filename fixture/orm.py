from pony.orm import *
#from datetime import datetime
from pymysql.converters import decoders
from model.group import Group
from model.contact import Contact

class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_='group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda:  ORMFixture.ORMContact, table="address_in_groups", column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_='addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        email = Optional(str, column='email')
        groups = Set(lambda:  ORMFixture.ORMGroup, table="address_in_groups", column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password) #, conv=decoders) - с декодером код не идет: TypeError: no default type converter defined
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
       return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), first_name=contact.firstname, last_name=contact.lastname,
                           home_phone=contact.home_phone, mobile_phone=contact.mobile_phone, work_phone=contact.work_phone,
                           email=contact.email
                           )
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
       return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact))

    @db_session
    def get_contacts_in_group(self, group):
        orm_groups = self.get_first_group_fom_db(group)
        return self.convert_contacts_to_model(orm_groups.contacts)

    def get_first_group_fom_db(self, group):
        temp_group = group
        orm_groups = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return orm_groups

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.get_first_group_fom_db(group)
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if orm_group not in c.groups))