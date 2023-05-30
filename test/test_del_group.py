
from model.group import Group
from random import randrange
import random

def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    #поиск нужной группы и удаление ее по идентификатору
    group = random.choice(old_groups)
    #обращ-ся к функции и в кач параметра передаем индентифик группы
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    #удаление старого элемента из списка
    old_groups.remove(group)
    assert old_groups == new_groups

def test_delete_some_group_Ui(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    # удаление по индексу группы из интерфейса.
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups