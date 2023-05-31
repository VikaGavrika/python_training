#import pymysql.cursors
#from fixtura.db import DbFixture
from fixtura.orm import ORMFixture

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

#try:
    #cursor = connection.cursor()
    #cursor.execute("select * from group_list")
    #for row in cursor.fetchall():
        #print(row)
#finally:
    #connection.close()

#db = DBFixture(host="127.0.0.1", name="addressbook", user="root", password="")

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#try:
    #groups = db.get_group_list()
    #for group in groups:
        #print(group)
    #print(len(groups))
#finally:
    #db.destroy()

#try:
    #contacts = db.get_contact_list()
    #for contact in contacts:
        #print(contact)
    #print(len(contacts))
#finally:
    #db.destroy()

#универсальный вариант
try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()

#try:
    #l = db.get_group_list()
    #for item in l:
        #print(item)
    #print(len(l))
#finally:
    #pass #db.destroy()