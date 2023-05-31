
from model.group import Group
from random import randrange
import random

def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test2", footer="test3"))
    old_groups = db.get_group_list()
    new_data_group = Group(name="New group1", header="New group2", footer="New group3")
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, new_data_group)
    new_groups = db.get_group_list()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



def test_modify_group_UI(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
    #if app.group.count() == 0:
       # app.group.create(Group(name="test"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
