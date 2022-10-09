marks = []
st = []
n = int(input())
for i in range(0,n):
    name =input()
    arr = map(int,input().split())
    marks.clear()
    [marks.append(i) for i in arr]
    st.append([name,marks])


dictionary = [dict(= marks) for(name,marks) in st]
print(dictionary)