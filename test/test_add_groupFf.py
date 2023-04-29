# -*- coding: utf-8 -*-


from model.group import Group


def test_add_group_f_f(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="123", header="1234", footer="12345"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_emptygroup_f_f(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)




