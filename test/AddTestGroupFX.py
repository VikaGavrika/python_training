# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixtura.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_test_group_f_x(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="123456", header="654321", footer="123456"))
    app.session.logout()
def test_add_test_emptygroup_f_x(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()



