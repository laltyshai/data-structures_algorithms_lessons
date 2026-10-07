# selection sorting
array = [99,2,5,3,77,67]
array2 = [-333,8,7,6,1,0,9,2]
arr3=[]
array4= [3,1,4,1,3,1]

def countingSort(ar):
    print(ar)
    counter = [0]*max(ar)
    for i in range(len(ar)):
        if counter[ar[i]] !="none":
            counter[ar[i]]+=1
        else:
            counter[ar[i]]=ar[i]
    print(counter)
    res = [0]*len(ar)
    # for j in range(len(counter)):
    #     res[counter[j]]=j
    #     counter[j]-=1
    for j in ar:
        print(j, counter[j])
        counter[j]-=1
        res[counter[j]]=j
        
        
    return res





def countingSort2(ar):
    if not ar:
        return []
    lo, hi = min(ar), max(ar)
    counter = [0] * (hi - lo + 1)   # one slot per value from lo to hi

    for x in ar:                    # 1. count each value
        counter[x - lo] += 1
    for i in range(1, len(counter)):    # 2. running total = end position
        counter[i] += counter[i - 1]

    res = [0] * len(ar)
    for x in reversed(ar):          # 3. place from the back, keeps it stable
        counter[x - lo] -= 1
        res[counter[x - lo]] = x
    return res

for arr in (array, array2, arr3, array4):
    print(countingSort2(arr), "expected", sorted(arr))