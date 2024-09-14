from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    app.contact.modify_first(Contact("contactEdited", "mnameEdited", "lnameEdited", "1234567890", "aEdited@ya.ru"))

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    app.contact.modify_first(Contact(middle_name = "mnameEdited1"))

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact_created_to_be_modified"))
    app.contact.modify_first(Contact(last_name = "lnameEdited2"))