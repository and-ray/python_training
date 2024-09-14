from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group_created_to_be_deleted"))
    app.group.delete_first_group()
