# numbers = [5,2,5,2,2]
# for count in numbers:
#     print('*'*count)

numbers  = [5,2,5,2,2]
for count in numbers:
    output = ''
    for item in range(count):
        output += 'x'
    print(output)

print()
numbers  = [2,2,2,2,5]
for count in numbers:
    output = ''
    for item in range(count):
        output += 'x'
    print(output)