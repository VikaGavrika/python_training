from model.contact import Contact
from model.group import Group
from fixtura.orm import ORMFixture
import random


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="Name1", firstname="NameName2", address="addr3"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test2", footer="test3"))
    #список групп
    groups = orm.get_group_list()
    #рандомная группа
    group = random.choice(groups)
    #список контактов в группе, это потом для проверки
    contacts_in_groups = orm.get_contacts_in_group(group)
    #список контактов, которые еще не состоят в группе
    contacts_without_group = orm.get_contacts_without_group(group)
    #если есть такой контакт
    if len(orm.get_contacts_without_group(group)) != 0:
        # случайный контакт из списка контактов, которые не в группе
        contact = random.choice(contacts_without_group)
        # добавляем контакт в группу
        app.contact.add_contact_by_id_to_group(contact.id, group.id)
    #если нет такого контакта, то создаем его
    else:
        app.contact.create(Contact(lastname="1", firstname="2", address="3"))
        contacts_without_group2 = orm.get_contacts_without_group(group)
        contact = random.choice(contacts_without_group2)
        # добавляем контакт в группу
        app.contact.add_contact_by_id_to_group(contact.id, group.id)
    assert len(contacts_in_groups) + 1 == len(orm.get_contacts_in_group(group))
    assert orm.contact_in_group(group, contact) is True


#список всех групп
#выбрать какую-то группу
#Список контактов,которые не состоят в гурппах
#Если нет таких контактов, то нужно создать контакт не состоящий в гурппе
#Выбираем случайный контакт из списка контактов не в гурппею Айди
#Добавляем этот контакт в выбранную ранее группу
#Для проверок: Старый список контактов в группе должен быть больше на 1,чем новый список контактов в группе
# Проверка2: дейсвтивтельно ли контакт в группе- Тру

