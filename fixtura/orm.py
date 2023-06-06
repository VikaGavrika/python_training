from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        lastname = Optional(str, column="lastname")
        firstname = Optional(str, column="firstname")
        address = Optional(str, column="address")
        homephone = Optional(str, column="home")
        mobile = Optional(str, column="mobile")
        workphone = Optional(str, column="work")
        phone2 = Optional(str, column="phone2")
        email = Optional(str, column="email")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts",
                       lazy=True)

    #описываем привязку к БД
    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    #реализуем функции, которые получают списки обьектов
    def get_group_list(self):
        #SQL запрос не пишем, pony будет генерить автоматически. пишем запрос с выборкой из набора объектов класса
        # блок кода должен выполняться в рамках сессии
        with db_session:
            return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), lastname=contact.lastname, firstname=contact.firstname, address=contact.address,
                           homephone=contact.homephone, mobile=contact.mobile, workphone=contact.workphone, phone2=contact.phone2,
                           email=contact.email, email2=contact.email2, email3=contact.email3)
        return list(map(convert, contacts))

    #либо можно пометить целую функцию
    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_without_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_groups_with_contacts(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup if len(g.contacts) > 0))

    @db_session
    def contact_in_group(self, group, contact):
        group = Group(id=group.id)
        contacts_in_group = self.get_contacts_in_group(group)
        for contact in contacts_in_group:
            if contact.id == contact.id:
                return True
        return False

    @db_session
    def get_contacts_list_NOT_in_groups(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None and len(c.groups) ==0))








