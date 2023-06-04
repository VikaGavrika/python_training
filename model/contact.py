from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, homephone=None, mobile=None,
                       workphone=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None,
                       phone2=None, notes=None, id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % \
            (self.id, self.lastname, self.firstname, self.address,
             self.homephone, self.mobile, self.workphone, self.phone2, self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
            (self.lastname == other.lastname or self.lastname is None or other.lastname is None) and \
            (self.firstname == other.firstname or self.firstname is None or other.firstname is None) and \
            (self.address == other.address or self.address is None or other.address is None) and \
            (self.homephone == other.homephone or self.homephone is None or other.homephone is None) and \
            (self.mobile == other.mobile or self.mobile is None or other.mobile is None) and \
            (self.workphone == other.workphone or self.workphone is None or other.workphone is None) and \
            (self.phone2 == other.phone2 or self.phone2 is None or other.phone2 is None) and \
            (self.email == other.email or self.email is None or other.email is None) and\
            (self.email2 == other.email2 or self.email2 is None or other.email2 is None) and\
            (self.email3 == other.email3 or self.email3 is None or other.email3 is None)



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize



