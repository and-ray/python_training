# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    new_contact = Contact("contact1FirstNameCheckLocator", "mname", "lname", "1234567890", "a@ya.ru")
    app.contact.create(new_contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contact_list = app.contact.get_contact_list()
    new_contact = Contact("", "", "", "", "")
    app.contact.create(new_contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

