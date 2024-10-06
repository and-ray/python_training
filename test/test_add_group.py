# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_group_list = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

