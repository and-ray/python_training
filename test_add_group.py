# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login( "admin", "secret")
    app.create_group( Group(name="group_1_recording", header="group_1_header", footer="group_1_footer"))
    app.logout()

def test_add_empty_group(app):
    app.login( "admin", "secret")
    app.create_group( Group(name="", header="", footer=""))
    app.logout()
