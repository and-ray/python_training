import random

from model.contact import Contact


def test_delete_contact_by_index(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name = "Contact_created_to_be_deleted"))
    old_contact_list = db.get_contact_list()
    contact_to_delete = random.choice(old_contact_list)
    app.contact.delete_contact_by_id(contact_to_delete.id)
    new_contact_list = db.get_contact_list()
    old_contact_list.remove(contact_to_delete)
    assert old_contact_list == new_contact_list
    if check_ui:
        assert sorted(new_contact_list, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)


