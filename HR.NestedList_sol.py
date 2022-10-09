# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])
# second_highest = sorted(list(set([marks for (name, marks) in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
#


list_name = []
N = int(input())
for i in range(0,N):
    list_name.append([input(),float(input()),int(input())])
print(list_name)
for j in list_name :
    
# val = sorted(list(marks for(name,marks) in list_name))
# print(val)
#
# print(name for(name,marks) in list_name for(marks) in val)

# print("\n".join(sorted(name for(name,marks) in list_name if marks==second_highest)))