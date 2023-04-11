# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_test_group_f_x(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="12345", header="54321", footer="12345"))
    app.logout()
def test_add_test_emptygroup_f_x(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()



