import random

from model.group import Group

def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "Group_created_to_be_modified"))
    old_group_list = db.get_group_list()
    group_to_modify = random.choice(old_group_list)
    modify_data = Group(name="nameEdited22222", header="headerEdited22222", footer="footerEdited22222", id=group_to_modify.id)
    app.group.modify_by_id(modify_data, group_to_modify.id)
    new_group_list = db.get_group_list()
    assert len(old_group_list) == len(new_group_list)
    old_group_list[old_group_list.index(group_to_modify)] = modify_data
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)


def test_modify_group_name(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "Group_created_to_be_modified"))
    old_group_list = db.get_group_list()
    group_to_modify = Group(name = "nameEdited2")
    group_to_modify.id = old_group_list[0].id
    app.group.modify_first(group_to_modify )
    new_group_list = db.get_group_list()
    assert len(old_group_list) == len(new_group_list)
    old_group_list[0] = group_to_modify
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

def test_modify_group_header(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "Group_created_to_be_modified"))
    old_group_list = db.get_group_list()
    app.group.modify_first(Group(header = "headerEdited3"))
    new_group_list = db.get_group_list()
    assert len(old_group_list) == len(new_group_list)

def test_modify_group_footer(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "Group_created_to_be_modified"))
    old_group_list = db.get_group_list()
    app.group.modify_first(Group(footer = "footerEdited4"))
    new_group_list = db.get_group_list()
    assert len(old_group_list) == len(new_group_list)