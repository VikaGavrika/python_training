# -*- coding: utf-8 -*-


from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*6
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(lastname="", firstname="", address="")] + [
    Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 8),
            address=random_string("address", 10))
    for i in range(2)]

#testdata = [
    #Contact(lastname="", firstname="", address=""),
    #Contact(lastname="eee", firstname="wwww", address="qqqq")]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




