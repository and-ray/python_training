# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from datetime import datetime
import random

def test_add_contact(app, db, json_contacts, check_ui):
    new_contact = json_contacts
    old_contact_list = db.get_contact_list()
    app.contact.create(new_contact)
    new_contact_list = db.get_contact_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)

def test_add_contact_to_group(app, db, json_contacts, check_ui):
    group = Group(name = "Group_created_"+str(datetime.now().time()), header="header lalala", footer="footer lalala")
    app.group.create(group)
    group.id = app.group.get_id(group.name)
    new_contact = json_contacts
    new_contact.first_name = new_contact.first_name + str(datetime.now().time())
    app.contact.create(new_contact)
    new_contact.id = app.contact.get_id(new_contact.first_name)
    app.contact.add_contact_to_group(new_contact, group.name)
    # вытаскиваю из БД контакты с нужной группой
    new_contacts_fom_db = db.get_contacts_in_group(group)

    # проверяю данные исходные с тем, что получено из БД по контакту.
    assert new_contact in new_contacts_fom_db

