# selection sorting
array = [99,2,5,3,77,67]
array2 = [-333,8,7,6,1,0,9,2]
arr3=[]

def bubbleSort(ar):
    for j in range(len(ar)):
        for i in range(len(ar)-1-j):
            if ar[i]> ar[i+1]:
                ar[i], ar[i+1] = ar[i+1], ar[i]
    return ar
print(bubbleSort(arr3))
                