# selection sorting
array = [99,2,5,3,77,67]
array2 = [-333,8,7,6,1,0,9,2]

# def selectionSort(ar):
    
#     for i in range(len(ar)):
#         min = ar[i]
#         min_index=i
#         for j in range(i+1, len(ar)):
#             if ar[j]<min:
#                 min=ar[j]
#                 min_index=j
#         ar[min_index]=ar[i]
#         ar[i]=min
#     return ar
# print(selectionSort(array2))
                
def selection(ar):
    for i in range(len(ar)):
        minim = ar[i]
        minind=i
        for j in range(i, len(ar)):
            if ar[j]<minim:
                minim=ar[j]
                minind=j
        ar[minind]=ar[i]
        ar[i]=minim

    print(ar)
    return ar
print(array2)
print(selection(array2)==sorted(array2))

