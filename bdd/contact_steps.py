

from pytest_bdd import given, when, then, parsers
from model.contact import Contact
import random


@given("a contact list",  target_fixture="contact_list")
#шаги с given представляют собой фикстуры их можно передавать в кач параметров в другие фикстуры и тесты
def contact_list(db):
    #через фикстуру берем список групп и возвращаем его
    return db.get_contact_list()

@given(parsers.parse("a contact with {firstname}, {lastname}"), target_fixture="new_contact")
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when("I add the contact to the list")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given("a non-empty contact list", target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(firstname="1"))
    return db.get_contact_list()

@given("a random contact from the list", target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)
@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then("the new contact list is equal to the old list without the deleted contact")
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@when("I modify the contact from the list")
def modify_contact(app, random_contact, new_contact):
    new_contact.id = random_contact.id
    app.contact.modify_contact_by_id(random_contact.id, new_contact)

@then("the new contact list is equal to the old list with the modified contact")
def verify_contact_modified(db, check_ui, app, non_empty_contact_list, new_contact, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_group_list()
    old_contacts.remove(random_contact)
    old_contacts.append(new_contact)
    old_contacts = db.get_group_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test1", firstname="test2", address="test3"))
    old_contacts = db.get_contact_list()
    new_contact_data = Contact(lastname="NewNew1", firstname="NewNew2", address="NewNew3")
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    app.contact.modify_contact_by_id(contact.id, new_contact_data)
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contact_data
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
