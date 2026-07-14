# By Raj Shekhar Aryal
# Simple site connection checker

import urllib.request as urllib

def connect(url):
    print("Checking connectivity")
    response = urllib.urlopen(url)
    print("Connected to", url, "sucessfully")
    print("Respose code is :",response.getcode())


url = input("Please enter the url :")

connect(url)
