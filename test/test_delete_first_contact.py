from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "Contact_created_to_be_deleted"))
    app.contact.delete_first_contact()
