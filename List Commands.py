n = int(input())
listing = []
count = 0
while count!=n :
    name, *line = input().split()
    if name =='insert':
        number = list(map(int, line))
        listing.insert(number[-2],number[-1])
    if name == 'print':
        print(listing)
    if name == 'remove':
         number = list(map(int, line))
         listing.remove(number[-1])
    if name == 'append':
         number = list(map(int, line))
         listing.append(number[-1])
    if name =='sort':
        listing.sort()
    if name =='pop':
        listing.pop()
    if name=='reverse':
        listing.reverse()
    count+=1
