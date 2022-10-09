n = int(input())
student = []
# [ student.append([input(),float(input())]) for i in range(0,n)]
scores = []
 # [score.append([score]) for(name,score) j in student]
# print(student)
# print(score)
for i in range(0,n):
    student.append([input(),float(input())])
scores.sort()
# second= scores[1]
lst= []
[lst.append(title) for(title,mark) in student if mark==scores[1]]
print(lst)


