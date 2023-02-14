# printed in list format

text = 'geeks for geeks'

# Splits at space
print(text.split())

word = 'geeks, for, geeks'

# Splits at ','
print(word.split(','))

word = 'geeks:for:geeks'

# Splitting at ':'
print(word.split(':'))

word = 'CatBatSatFatOr'

# Splitting at 3
print([word[i:i + 3] for i in range(0, len(word), 3)])

word = 'geeks, for, geeks, pawan'

# maxsplit: 0
print(word.split(', ', 0))

# maxsplit: 4
print(word.split(', ', 4))

# maxsplit: 1
print(word.split(', ', 1))

