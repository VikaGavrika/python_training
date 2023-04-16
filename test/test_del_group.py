
def test_delete_first_group_f_f(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()