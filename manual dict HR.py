n = int(input())
keys = []
values = []
for i in range(0,n):
    keys.append(input())
    values.append(list(map(float,input().split())))
dictionary = dict(zip(keys,values))
print(dictionary)
name = input()
sum = 0
list = []
if name in dictionary:
    l = len(dictionary.get(name))
    for i in dictionary.get(name):
        sum += i
    average = sum/l
print("%.2f"%average)


