# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact("contact1FirstName", "mname", "lname", "1234567890", "a@ya.ru"))

def test_add_empty_contact(app):
    app.contact.create(Contact("", "", "", "", ""))

