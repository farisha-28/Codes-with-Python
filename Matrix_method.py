numbers = [3,5,2,7,6,4]
numbers.append(45)
numbers.pop()
print(numbers)
numbers.clear()
numbers.insert(0,3)
numbers.insert(1,6)
numbers.insert(2,8)
numbers.insert(3,1)
numbers.insert(4,10)
# pass the value that needs to be deleted
numbers.remove(8)
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
print(numbers)
print(numbers.count(1))
# returns boolean
print(numbers.index(6))
# print(numbers.index(9))
print(9 in numbers)
print(numbers2)