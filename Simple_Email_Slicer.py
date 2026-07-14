# By Raj Shekhar Aryal
# Simple email slicer made in python

email = input("Please enter your email address : ")

def email_slicer (email):
    (email,domain) = email.split('@')
    (domain,extension) = domain.split('.')

    print("Email : ", email)
    print("Domain : ", domain)
    print("Extension : ", extension)

email_slicer(email)

