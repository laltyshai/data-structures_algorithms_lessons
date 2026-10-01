# insertion sorting
array = [99,2,5,3,77,67]
array2 = [-333,8,7,6,1,0,9,2]

def insertionSort(ar):
    for j in range(0, len(ar)):
            for k in range(j, 0, -1):
                if ar[k-1]>ar[k]:
                    ar[k-1], ar[k]= ar[k], ar[k-1]
                    print("swapped")
    return ar
print(insertionSort(array2))

def insertionSort2(ar):
    for i in range(1, len(ar)):
        key = ar[i]               
        j = i - 1
        while j >= 0 and ar[j] > key:
            ar[j + 1] = ar[j]     
            j -= 1
        ar[j + 1] = key            
    return ar

print(insertionSort2(array2))


                