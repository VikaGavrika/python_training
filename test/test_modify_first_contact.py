

from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="New Petr"))


