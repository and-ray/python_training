from model.contact import Contact

def test_modify_first_contact(app):
    app.contact.modify_first(Contact("contactEdited", "mnameEdited", "lnameEdited", "1234567890", "aEdited@ya.ru"))
