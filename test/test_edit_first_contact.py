

from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="Volodya1", middlename="Petrovich1", lastname="Volkov1", nickname="Volk1", tittle="Pik1",
                company="Puki1", address="gorod1", homephone="9-999-991",
                mobile="9-999-999-99-991", workphone="9-991", fax="91", email="volkov@volkov1", email2="volkov2@volkov1",
                email3="volkov3@volkov1",
                homepage="volkov0volkov1", bday="21", bmonth="December", byear="2001", aday="11", amonth="July",
                ayear="2011", address2="gorod21", phone2="8-888-881",
                notes="pipipuk1"))
    app.session.logout()

