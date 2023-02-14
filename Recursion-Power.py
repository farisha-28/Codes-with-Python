def myRecursion(x, n):
    if n==0:
        return 1;
    else:
        return x*myRecursion(x, n-1)


x = int(input())
n = int(input())
df = myRecursion(x, n)
print(df)
