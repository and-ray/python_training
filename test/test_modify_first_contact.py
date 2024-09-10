from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact("contactEdited", "mnameEdited", "lnameEdited", "1234567890", "aEdited@ya.ru"))
    app.session.logout()