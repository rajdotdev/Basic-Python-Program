# By Raj Shekhar Aryal
# Simple Password Generator in python

import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")


def password():
    random.shuffle(characters)
    passwords = []

    length = int(input("Please enter your required length of the password :"))

    for i in range(length):
        passwords.append(random.choice(characters))

    random.shuffle(passwords)

    print(''.join(passwords))


password()
