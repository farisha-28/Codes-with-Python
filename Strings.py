course = "Learning python for the first time."
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.title())
print(course.find('Python'))
print(course.find('Learning'))
print(course.replace('python','Basic python'))
print(course.replace('Python','Basic python'))
print('first' in course)
print('First' in course)
print(course.isalpha())

#  . (space)!#%&? are not alpha
text = 'Serte'
print(text.isalpha())

string = "let's do some Productive things."
print(string.capitalize())

print(course[5])
print(course[0:-1])
print(course[2:-1])
print(course[0: ])
print(course[ : ])
print(course[ :-1])
print(course[ :-2 ])

first = 'Farisha'
last = 'Hussain'
# message = first+' ['+last+'] '+'is a coder.'
formatted_str = f'{first} [{last}] is a coder.'
print(formatted_str)
# print(message)