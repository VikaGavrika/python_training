
from model.group import Group
def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group((Group(name="1111111", header="22222", footer="333333")))
    app.session.logout()