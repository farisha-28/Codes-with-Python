num = int(input())
if 1<=num<=150:
    output = ""
    for item in range(num):
       output += str(item+1)
print(output)
