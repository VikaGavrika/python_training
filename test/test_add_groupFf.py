# -*- coding: utf-8 -*-


from model.group import Group


def test_add_group_f_f(app):
    app.group.create(Group(name="1234567", header="654321", footer="123456"))

def test_add_emptygroup_f_f(app):
    app.group.create(Group(name="", header="", footer=""))




