from random import randint

array = [-333,8,7,6,1,0,9,2]
arr1= [randint(1,100) for _ in range(10)]
def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left_sorted= merge_sort(arr[mid:])
    right_sorted= merge_sort(arr[:mid])
    return merge(left_sorted, right_sorted)

def merge(ar1, ar2):
    i,j=0,0
    res=[]
    while i<len(ar1) and j < len(ar2):
        if ar1[i]<ar2[j]:
            res.append(ar1[i])
            i+=1
        elif ar1[i]>=ar2[j]:
           res.append(ar2[j])
           j+=1 
    res+=ar1[i:]
    res+=ar2[j:]
    return res

print(arr1)
print("\n .............")
print(merge_sort(arr1))



# version2
def mergesort(ar):
    length = len(ar)
    if len(ar) == 1:
        return ar
    mid = length//2
    l = mergesort(ar[mid:])
    r = mergesort(ar[:mid])
    return merge1(l,r)
def merge1(l,r):
    i,j=0,0
    res=[]
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
    res+=l[i:]
    res+=r[j:]
    return res
print(arr1)
print("\n .............")
print(mergesort(arr1))