from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group_created_to_be_modified"))
    app.group.modify_first(Group("nameEdited", "headerEdited", "footerEdited"))

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group_created_to_be_modified"))
    app.group.modify_first(Group(name = "nameEdited2"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group_created_to_be_modified"))
    app.group.modify_first(Group(header = "headerEdited3"))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group_created_to_be_modified"))
    app.group.modify_first(Group(footer = "footerEdited4"))