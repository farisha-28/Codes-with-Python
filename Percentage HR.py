n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    # adding element in a dictionary
    student_marks[name] = scores
print(student_marks)
query_name = input()
sum = 0
list = []
if query_name in student_marks:
    l = len(student_marks.get(query_name))
    for i in student_marks.get(query_name):
        sum += i
    average = sum/l
print("%.2f"%average)


