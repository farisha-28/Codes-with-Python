
def printArr(array):
    for item in range(len(array)):
        print(array[item], end=" ")
    print()

def merge_Array(array,mid,left,right):

    i=j=z=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[z] = left[i]
            i += 1
        else:
            array[z] = right[j]
            j += 1
        z += 1

    while i < len(left):
        array[z] = left[i]
        i += 1
        z += 1

    while j < len(right):
        array[z] = right[j]
        j += 1
        z += 1


def merge_Sorting(array):

    if len(array) > 1:

        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        merge_Sorting(left)
        merge_Sorting(right)
        merge_Array(array,mid,left,right)

size = int(input())
array = list(map(int,input().strip().split()))[:size]
merge_Sorting(array)
print("Merge Sorted array : ")
printArr(array)