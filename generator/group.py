from model.group import Group

import random
import string
import json
import os.path

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*3
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 8), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(5)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..//data/groups.json")

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))