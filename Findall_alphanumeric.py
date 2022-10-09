import re
xx = "guru99,education is fun"
r1 = re.search(r"^\w+",xx)
print(r1)

# "^": This expression matches the start of a string
# "w+": This expression matches the alphanumeric character in the string
# if you remove +sign from the w+, the output will change, and it will only give the first character of the first letter, i.e., [g]