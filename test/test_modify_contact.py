import random
from model.contact import Contact

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    old_contact_list = db.get_contact_list()
    contact_to_modify = random.choice(old_contact_list) #с 0
    modify_data = Contact(id=contact_to_modify.id, first_name="contactEdited2", middle_name="mnameEdited2", last_name="lnameEdited2", work_phone="1234567890", address ="Earth 3d", email="alkjkjkjk@ya.ru")
    app.contact.modify_by_id(modify_data, contact_to_modify.id)
    new_contact_list = db.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[old_contact_list.index(contact_to_modify)] = modify_data
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)

def test_modify_first_contact_middlename(app,  db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    old_contact_list = db.get_contact_list()
    app.contact.modify_first(Contact(middle_name = "mnameEdited1"))
    new_contact_list = db.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)

def test_modify_first_contact_lastname(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    old_contact_list = db.get_contact_list()
    app.contact.modify_first(Contact(last_name = "lnameEdited2"))
    new_contact_list = db.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)