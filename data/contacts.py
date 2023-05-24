from model.contact import Contact
import random
import string

testdata = [
    Contact(lastname="", firstname="", address=""),
    Contact(lastname="lastname1", firstname="firstname1", address="address1")
]
#constant = [
    #Contact(lastname="", firstname="", address=""),
    #Contact(lastname="lastname1", firstname="firstname1", address="address1")
#]

#def random_string(prefix, maxlen):
    # *1 пробел среди символов, с бОльшим кол-вом тесты не проходят проверку часто.
   # symbols = string.ascii_letters + string.digits + " "*1
   # return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [Contact(lastname="", firstname="", address="")] + [
    #Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 8),
            #address=random_string("address", 10))
    #for i in range(2)]

#testdata = [
    #Contact(lastname="", firstname="", address=""),
    #Contact(lastname="eee", firstname="wwww", address="qqqq")]