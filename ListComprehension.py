x = int(input())
y = int(input())
z = int(input())
n = int(input())




permutation  = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n ]
print(permutation)




# indices  = [[i+1,j+1] for i in range(0,mid) for j in range(i+1,mid) if A[i]+A[j]==mid]
# print(indices)

for i in range(0,mid):
    for j in range(i+1,mid):
        if A[i]+A[j]==mid:
            print(cfsdhfsdhkfhk)
            break;