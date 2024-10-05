# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string (prefix, maxlen):
    symbols = string.ascii_letters + " " + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits (prefix, maxlen):
    symbols = string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email (prefix):
    symbols = string.ascii_letters + string.digits
    domain = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(10))])+"@"+"".join([random.choice(domain) for i in range(random.randrange(10))])+".ru"


testData = [
Contact(first_name=first_name, middle_name=middle_name, last_name=last_name,
        home_phone=home_phone,work_phone=work_phone, mobile_phone=mobile_phone, email1=email1)
    for first_name in ["", random_string("first_name", 10)]
    for middle_name in [random_string("middle_name", 20)]
    for last_name in ["", random_string("last_name", 20)]
    for home_phone in [random_digits("home_phone", 20)]
    for work_phone in [random_digits("work_phone", 20)]
    for mobile_phone in [random_digits("mobile_phone", 20)]
    for email1 in [random_string("email1", 20)]
]

@pytest.mark.parametrize("new_contact", testData, ids=[repr(x) for x in testData])
def test_add_contact(app, new_contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(new_contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


