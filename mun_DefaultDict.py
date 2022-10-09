from collections import defaultdict

n,m = map(int,input().split())
dic= defaultdict(list)
for item in range(n):
    word = input()
    dic[word].append(item+1)
for i in range(m):
    find = input()
    if find in dic.keys():
        print(*dic[find])
    else:
        print("-1")