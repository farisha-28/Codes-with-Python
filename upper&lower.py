string  = input()
print(string.swapcase())

# The .count() method adds up the number of times a character or sequence of characters appears in a string. For example:
#
# >>> s = "That that is is that that is not is not is that it it is"
# >>> s.count("t")
# 13
# Why didn’t it count all of the t‘s? Because ‘T’ is a different character from ‘t’. So, if we want to count all of the t‘s.
#
# >>> s = s.lower()
# >>> s.count("t")
# 14
# We can also count entire words, which, as we know, are sequences of characters:
#
# s = "James while John had had had had had had had had had had had a better effect on the teacher"
# >>> s.count("had")
# 11