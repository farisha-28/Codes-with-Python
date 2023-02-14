size = int(input())
array = list(map(int, input().strip().split()))[:size]
print(array)
sum = 0
max_so_far = 0
for item in range(0, size):
    sum += array[item]
    if sum < 0:
        sum = 0
    else:
        max_so_far = max(sum, max_so_far)
print(max_so_far)
