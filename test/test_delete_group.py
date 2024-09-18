from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group_created_to_be_deleted"))
    old_group_list = app.group.get_group_list()
    app.group.delete_first_group()
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list[0:1]=[]
    assert old_group_list == new_group_list
