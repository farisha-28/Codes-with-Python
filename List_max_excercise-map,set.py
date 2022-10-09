# numbers = [1,5,5,3,7,9,9,2]
# maximum= max(numbers)
# # for num in numbers:
# #     if max<num:
# #         max = num
# numbers.remove(maximum)
#

# list1 = [11,22,1,2,5,67,21,32,32,11]
# # to get unique elements
# new_list = set(list1)
# # removing the largest element from list1
# print(new_list)
# new_list.remove(max(new_list))
# # now computing the max element by built-in method?
# print(max(new_list))

# Second max or runner up with space seperated input
n = int(input())
arr = map(int, input().split())
new_arr = set(arr)
print(new_arr)
jdk = sorted(arr)
print(jdk)
new_arr.remove(max(new_arr))
print(max(new_arr))
