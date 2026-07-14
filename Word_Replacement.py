# By Raj Shekhar Aryal
# Simple Word Replacement program in python

string = input("Please enter your desired sentence : ")

def word_replacement(str):
    replace = input("Enter what you would like to replace : ")
    replace_to = input("Enter what you would like to replace it with : ")
    print(f" Your string after changing [{replace}] with [{replace_to}] becomes \n {str.replace(replace,replace_to)}")


word_replacement(string)

