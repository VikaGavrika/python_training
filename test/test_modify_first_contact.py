

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="newtest", lastname="new_test", address="gorod",
                mobile="9-999-999-99-99", email="volkov@volkov"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New_Name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


