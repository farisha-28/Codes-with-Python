s = input()
list1 = []
for i in s.lower():
    if i not in list1:
        c = s.count(i)
        print(f'"{i}" : {c}')
        list1.append(i)


