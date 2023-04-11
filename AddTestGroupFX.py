# -*- coding: utf-8 -*-

import unittest
from group import Group
from application import Application

class AddTestGroupFX(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_test_group_f_x(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="12345", header="54321", footer="12345"))
        self.app.logout()
    def test_add_test_emptygroup_f_x(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()