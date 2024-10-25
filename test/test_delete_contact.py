import random
from model.group import Group
from model.contact import Contact
from datetime import datetime


def test_delete_contact(app, db,  check_ui):
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

def test_delete_contact_from_group(app, db, json_contacts, check_ui):
    # создаю контакт сразу в группе
    group = Group(name="Group_created_" + str(datetime.now().time()), header="header lalala", footer="footer lalala")
    app.group.create(group)
    group.id = app.group.get_id(group.name)
    new_contact = json_contacts
    new_contact.first_name = new_contact.first_name + str(datetime.now().time())
    # создаем контакт, включенный в группу, через UI
    app.contact.create_with_group(new_contact, group)
    new_contact.id = app.contact.get_id(new_contact.first_name)

    #удаляю контакт из группы
    app.group.select_on_contact_page(group)
    app.contact.select_contact_to_delete_from_group(new_contact)
    app.contact.delete_contact_from_group()

    # вытаскиваю из БД контактs с нужной группой
    new_contact_fom_db = db.get_contacts_not_in_group(group)

    # проверяю данные исходные без группы с тем, что получено из БД по контакту.
    assert new_contact in new_contact_fom_db


