# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact("contact1FirstName", "mname", "lname", "1234567890", "a@ya.ru"))
    app.logout()

def test_add_empty_contact(app):
    app.login( username="admin", password="secret")
    app.create_new_contact(Contact("", "", "", "", ""))
    app.logout()

