# create empty dic . allow 4 friends to enter their favbourite language as value and use key as their names . names- unique

d = {}

name = input ("enter friend name:")
lang = input("enter fav language name: ")
d.update({name : lang})
name = input ("enter friend name:")
lang = input("enter fav language name: ")
d.update({name : lang})
name = input ("enter friend name:")
lang = input("enter fav language name: ")
d.update({name : lang})
name = input ("enter friend name:")
lang = input("enter fav language name: ")
d.update({name : lang})
name = input ("enter friend name:")
lang = input("enter fav language name: ")
d.update({name : lang})


print(d)