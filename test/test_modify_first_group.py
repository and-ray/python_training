from model.group import Group

def test_modify_first_group(app):
    app.group.modify_first(Group("nameEdited", "headerEdited", "footerEdited"))

def test_modify_group_name(app):
    app.group.modify_first(Group(name = "nameEdited2"))

def test_modify_group_header(app):
    app.group.modify_first(Group(header = "headerEdited3"))
