
from model.group import Group
def test_delete_first_group_f_f(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
