# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from applying import Applying

@pytest.fixture
def app(request):
    fixture = Applying()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_test_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Volodya", middlename="Petrovich", lastname="Volkov", nickname="Volk", tittle="Pik", company="Puki", address="gorod", homephone="9-999-99",
                            mobile="9-999-999-99-99", workphone="9-99", fax="9", email="volkov@volkov", email2="volkov2@volkov", email3="volkov3@volkov",
                            homepage="volkov0volkov", bday="21", bmonth="December", byear="2000", aday="31", amonth="July", ayear="2010", address2="gorod2", phone2="8-888-88",
                            notes="pipipuk"))
    app.logout()


