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

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        lastname = Optional(str, column="lastname")
        firstname = Optional(str, column="firstname")
        address = Optional(str, column="address")
        deprecated = Optional(str, column="deprecated")

    #описываем привязку к БД
    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password, conv=decoders)
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
            return Contact(id=str(contact.id), lastname=contact.lastname, firstname=contact.firstname, address=contact.address)
        return list(map(convert, contacts))

    #либо можно пометить целую функцию
    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))


