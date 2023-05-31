

from model.contact import Contact
import random
from random import randrange

def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test1", firstname="test2", address="test3"))
    old_contacts = db.get_contact_list()
    new_contact_data = Contact(lastname="NewNew1", firstname="NewNew2", address="NewNew3")
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, new_contact_data)
    new_contacts = db.get_contact_list()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



def test_modify_some_contact_UI(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="test2"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="NewNew2")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)