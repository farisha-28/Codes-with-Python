
n = int(input())
arr = list(map(int, input().strip().split()))[:n]
start = 0
end = 0
start_end = 0
max_so_far = arr[1]
max_end = arr[1]

# sum = 0
# max_so_far = 0
# for item in range(0, size):
#     sum += array[item]
#     if sum < 0:
#         sum = 0
#     else:
#         max_so_far = max(sum, max_so_far)
# print(max_so_far)

for item in range(0,n):
    max_end += arr[item]
    if max_end < arr[item]:
        max_end = arr[item]
        start_end = item

    if max_end>max_so_far:
        max_so_far = max_end
        end = item
        start = start_end
print(max_so_far)