import re
xx = """guru99*
careerguru99
selenium"""
k1 = re.findall(r"^[\w]+", xx)
k2 = re.findall(r"^\w", xx, re.MULTILINE)
k3 =re.findall(r"^\w", xx)
k4 =re.findall(r"^[\w*]+", xx)
k5 =re.findall(r"\w", xx)

# Normally an asterisk (*) means "0 or more of the previous thing" but in the example above, it does not have that meaning,
# since the asterisk is inside of the character class, so it loses its "special-ness".

print(k1)
print(k2)
print(k3)
print(k4)
print(k5)