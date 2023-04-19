# -*- coding: utf-8 -*-


from model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(firstname="Volodya", middlename="Petrovich", lastname="Volkov", nickname="Volk", tittle="Pik",
                company="Puki", address="gorod", homephone="9-999-99",
                mobile="9-999-999-99-99", workphone="9-99", fax="9", email="volkov@volkov", email2="volkov2@volkov",
                email3="volkov3@volkov",
                homepage="volkov0volkov", bday="24", bmonth="December", byear="2000", aday="31", amonth="July",
                ayear="2010", address2="gorod2", phone2="8-888-88",
                notes="pipipuk"))



