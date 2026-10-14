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