# The strip() method in-built function of Python is used to remove all the leading and trailing spaces from a string.
# Python code to illustrate the working of strip()
string = '   Geeks for Geeks   '

# Leading spaces are removed
print(string.strip())

# Geeks is removed
print(string.strip('   Geeks'))

# Not removed since the spaces do not match
print(string.strip('Geeks'))

# Python code to illustrate the working of strip()
string = '@@@@Geeks for Geeks@@@@@'

# Strip all '@' from beginning and ending
print(string.strip('@'))

string = 'www.Geeksforgeeks.org'

# '.grow' removes 'www' and 'org' and '.'
print(string.strip('.grow'))


def Count(string):
    print("Length before strip()")
    print(len(string))

    # Using strip() to remove white spaces
    str = string.strip()
    print("Length after removing spaces")
    return str


# Driver Code
string = "  Geeks for Geeks   "
print(len(Count(string)))

