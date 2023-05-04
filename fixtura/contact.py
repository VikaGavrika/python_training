from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        # fill group form
        self.fill_contact_form(contact)
        # enter new contact
        wd.find_element_by_xpath("//input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None


    def add_first_contact_to_group(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit addition
        wd.find_element_by_name("add").click()
        # go to group page
        wd.find_element_by_xpath("//div[@id='content']/div/i/a").click()
        # return home page
        self.open_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit edit
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit OK
        wd.switch_to.alert.accept()
        self.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.byear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys("%s" % text)


    def change_select_value(self, select_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(select_name).select_by_visible_text("%s" % text))


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                element = row.find_elements_by_tag_name("td")
                id = element[0].find_element_by_name("selected[]").get_attribute("value")
                text = element[1].text
                text2 = element[2].text
                self.contact_cache.append(Contact(lastname=text, firstname=text2, id=id))
        return list(self.contact_cache)

