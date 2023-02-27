#!/usr/bin/env python3

from flag import Flag
from flag import notFlag
import re

pattern = r'^[a-zA-Z_]*$'

def valid(text):
    return  re.match(pattern, text) 

class User:
    def __init__(self):
        self.__admin = False

    def isAdmin(self):
        if self.__admin:
            print(Flag)
        else :
            print(notFlag)
        exit()

user = User()

print("You only get one chance ...")
key = input("Key : ").strip()
value = input("Value : ").strip()


if valid(key) and valid(value):
    setattr(user,key,value)

user.isAdmin()
