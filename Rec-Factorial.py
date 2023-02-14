def myRecursion(x):
    if x==1:
        return 1;
    else:
        return x * myRecursion(x-1)


x = int(input())
df = myRecursion(x)
print(df)