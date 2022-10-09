from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(list)
flag=0
for element in range(1,n+1):
    d['A'].append(input())
list_1 = d.get('A')
for i in range(1,m+1):
    value = input()
    if value in list_1:
        ind = list_1.index(value)
        # print(' '.join(map(int,ind+1)))
        print(ind+1)
    else:
        print("-1")
    print()
