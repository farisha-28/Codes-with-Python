# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
#
# str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).
#
#
# str.isdigit()
# This method checks if all the characters of a string are digits (0-9).
#
# str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).
#
# str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).


string = input()
l = len(string)

flag_1 =0
for i in string:
    if i.isalnum():
        print("True")
        flag_1 = 1
        break
if flag_1!=1:
    print("False")
flag_2 =0
for i in string:
    if i.isalpha():
        print("True")
        flag_2 = 1
        break
if flag_2!=1:
    print("False")

flag_3 =0
for i in string:
    if i.isdigit():
        print("True")
        flag_3 =1
        break
if flag_3!=1:
    print("False")

flag_4 = 0
for i in string:
    if i.islower():
        print("True")
        flag_4 = 1
        break
if flag_4!=1:
    print("False")

flag_5 = 0
for i in string:
    if i.isupper():
        print("True")
        flag_5 = 1
        break
if flag_5!=1:
    print("False")
