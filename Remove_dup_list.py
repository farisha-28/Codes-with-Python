# numbers = [1,5,3,7,5,3,5,3,8,9,1,1]
# unique = []
# print(numbers)
# print()
# for value in numbers:
#     occured = numbers.count(value)
#     if occured>1:
#         unique.append(value)
# for item in unique:
#     numbers.remove(item)
# print(numbers)

numList = [2,4,6,3,2,4,6,8]
uniques = []
for item in numList:
    if item not in uniques:
        uniques.append(item)
print(uniques)