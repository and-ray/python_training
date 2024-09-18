from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "Contact_created_to_be_deleted"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list

