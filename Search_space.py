import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.span())
print("The first white-space character is located in position:", x.start())


import re

txt = "The rain in Spain Portugal"
x = re.search("Portugal", txt)
print(x)
print(x.start())