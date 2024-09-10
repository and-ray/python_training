# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("contact1FirstName", "mname", "lname", "1234567890", "a@ya.ru"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.create(Contact("", "", "", "", ""))
    app.session.logout()

