
import re

m = re.search(r'([a-zA-Z0-9])\1+', input().strip())

# \1 -- same value pashapashi match korabe (contents of group 1) and + -- one or more occurances
# \2 contents of group 2
# m = re.findall(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
