import re

txt = "Spain falls mainly falls in plain Spanieoalll aalllly aal!"
		#		1           2                    3    4

#Check if the string contains "a" followed by exactly two "l" characters:

# l two or more times

x = re.findall("al{2,}", txt)
#exactly l duita thaktei hobe
# x = re.findall("al{2}", txt)

# two to four times
# x = re.findall("al{2,4}", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
