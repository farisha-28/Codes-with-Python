import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)