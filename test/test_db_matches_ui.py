from fixture.contact import merge_emails_like_on_home_page, merge_phones_like_on_home_page
from model.group import Group
from model.contact import Contact

def test_group_list(app,db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_contact_list(app,db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip(),
                       all_emails_from_home_page = merge_emails_like_on_home_page(contact),
                       all_phones_from_home_page = merge_phones_like_on_home_page(contact))
    db_list = list(map(clean, db.get_contact_list()))

    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)