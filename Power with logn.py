
def myRecursion(x, n):
    if n == 0:
        return 1
    temp = myRecursion(x, n//2)
    if n%2==0:
        return temp*temp
    else:
        return x*temp*temp


x = int(input())
n = int(input())
df = myRecursion(x, n)
print(df)
