
import re
from random import randrange
from model.contact import Contact
from fixtura.db import DbFixture
from fixtura.orm import ORMFixture


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_phones_first_contact_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_first_contact_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.phone2]))))

def test_info_some_contact_on_home_page_UI(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="testtest", address="testik", homephone="+1234",
                                   mobile="12345", workphone="123456", fax="123", email="a@aa.aa",
                                   email2="b@aa.aa", email3="c@aa.aa", address2="testik2", phone2="321"))
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email2, contact.email3])))

def test_info_all_contacts_on_home_page_db(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="testtest", address="testik", homephone="1234",
                                   mobile="12345", workphone="123456", email="a@aa.aa",
                                   email2="b@aa.aa", email3="c@aa.aa", address2="testik2", phone2="321"))
    list_contacts_UI = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    list_contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(list_contacts_UI)):
        assert list_contacts_UI[i].all_phones_from_home_page == merge_phones_like_on_home_page(list_contacts_db[i])
        assert list_contacts_UI[i].all_emails_from_home_page == merge_emails_like_on_home_page(list_contacts_db[i])
        assert list_contacts_UI[i].firstname == list_contacts_db[i].firstname
        assert list_contacts_UI[i].lastname == list_contacts_db[i].lastname
        assert list_contacts_UI[i].address == list_contacts_db[i].address


def test_info_all_contacts_on_home_page_orm(app):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="testtest", address="testik", homephone="1234",
                                   mobile="12345", workphone="123456", email="a@aa.aa",
                                   email2="b@aa.aa", email3="c@aa.aa", address2="testik2", phone2="321"))
    list_contacts_UI = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    list_contacts_orm = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(list_contacts_UI)):
        assert list_contacts_UI[i].all_phones_from_home_page == merge_phones_like_on_home_page(list_contacts_orm[i])
        assert list_contacts_UI[i].all_emails_from_home_page == merge_emails_like_on_home_page(list_contacts_orm[i])
        assert list_contacts_UI[i].firstname == list_contacts_orm[i].firstname
        assert list_contacts_UI[i].lastname == list_contacts_orm[i].lastname
        assert list_contacts_UI[i].address == list_contacts_orm[i].address









