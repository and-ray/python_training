from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o =="-f":
        f  = a

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)

def random_string (prefix, maxlen):
    symbols = string.ascii_letters + " " + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits (prefix, maxlen):
    symbols = string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email (prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    domain = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])+"@"+"".join([random.choice(domain) for i in range(random.randrange(maxlen))])+".ru"


testdata = [
Contact(first_name=first_name, middle_name=middle_name, last_name=last_name,
        home_phone=home_phone,work_phone=work_phone, mobile_phone=mobile_phone, email=email)
    for first_name in ["", random_string("first_name", 10)]
    for middle_name in [random_string("middle_name", 20)]
    for last_name in ["", random_string("last_name", 20)]
    for home_phone in [random_digits("home_phone", 20)]
    for work_phone in [random_digits("work_phone", 20)]
    for mobile_phone in [random_digits("mobile_phone", 20)]
    for email in [random_email("email", 10)]
]


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))