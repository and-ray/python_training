# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from datetime import datetime

def test_add_contact(app, db, json_contacts, check_ui):
    new_contact = json_contacts
    old_contact_list = db.get_contact_list()
    app.contact.create(new_contact)
    new_contact_list = db.get_contact_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)

def test_add_contact_to_group(app, db, json_contacts, check_ui):
   # if len(db.get_group_list()) == 0:
    #для обеспечения уникальности имени группы предусловие убрала, т.к. в других тестах создаются группы с одинаковыми названиями.
    group = Group(name = "Group_created"+str(datetime.now().time()), header="lalala", footer="lalala")
    app.group.create(group)
    groups = db.get_group_list()
    group.id = list(filter(lambda x: x.name == group.name, groups))[0].id

    #лист контактов до создания контакта.
    new_contact = json_contacts

    #создаем контакт, включенный у группу, через UI
    app.contact.create_with_group(new_contact, group)

    # вытаскиваю из БД контактs с нужной группой
    new_contact_fom_db = db.get_contacts_in_group(group)[0]

    # проверяю данные исходные с тем, что получено из БД по контакту.
    assert new_contact == new_contact_fom_db

