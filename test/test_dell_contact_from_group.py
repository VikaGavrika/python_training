from model.contact import Contact
from model.group import Group
from fixtura.orm import ORMFixture
import random


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_dell_contact_from_group(app):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="Name1", firstname="NameName2", address="addr3"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test2", footer="test3"))
    # список контактов не состоящих в группе - для проверки
    contacts_list_not_in_groups = orm.get_contacts_list_NOT_in_groups()
    # список групп, в которых есть контакты
    groups = orm.get_groups_with_contacts()
    # если нет такой группы, то создаем ее
    if len(orm.get_groups_with_contacts()) == 0:
        app.contact.add_contact_to_group()
    # рандомная группа из списка групп с контактами
    group = random.choice(groups)
    # список контактов в группе
    contacts_in_groups = orm.get_contacts_in_group(group)
    # случайный контакт из списка контактов в группе
    contact = random.choice(contacts_in_groups)
    # удаляем контакт из группы
    app.contact.delete_contact_by_id_from_group(group.id, contact.id)
    assert len(contacts_list_not_in_groups) + 1 == len(orm.get_contacts_list_NOT_in_groups())
    assert orm.contact_in_group(group, contact) is False






#найти все группы в которых есть контакты
#найти рандомную группу с контактами - айди
# достать список контактов из группы с айди
# выбрать рандомный контакт- Айди
#удалить
# для проверок: список контактов не в группе ДО удаления должен быть +1 списка контактов не в гурппе ПОСЛЕ удаления
# для проверок: контакт в определенной группе- Фолс - действительно не найден по ацди