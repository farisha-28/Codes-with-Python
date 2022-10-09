import re

txt = "The rain in Spain fallie mainly in the plainnnnn!"

#Check if the string contains "ain" followed by 1 or more "x" characters:

#ain jotogula thake shob individually print hbe
#ain er por n er similar aro n thakle oi n gula shoho o ain print hbe

x = re.findall("ain*", txt)


print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



import re

txt = "The rain in Spaineol fallas mainly in the plain!"


#Check if the string contains "al" followed by 0 or more "x" characters:

# 0 index(a) jotogula ase single shob print hbe...
# 1 index(l) only 0(a) er por onek gula thakle allll evabe print hbe
x = re.findall("al*", txt)
			#   01

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
