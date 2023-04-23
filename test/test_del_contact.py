

from model.contact import Contact
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="testtest", lastname="testtesttest", address="gorod",
                mobile="9-999-999-99-99", email="volkov@volkov"))
    app.contact.delete_first_contact()
