from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    old_contact_list = app.contact.get_contact_list()
    contact_to_modify = Contact("contactEdited", "mnameEdited", "lnameEdited", "1234567890", "aEdited@ya.ru")
    contact_to_modify.id = old_contact_list[0].id
    app.contact.modify_first(contact_to_modify)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[0] = contact_to_modify
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.modify_first(Contact(middle_name = "mnameEdited1"))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.modify_first(Contact(last_name = "lnameEdited2"))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)