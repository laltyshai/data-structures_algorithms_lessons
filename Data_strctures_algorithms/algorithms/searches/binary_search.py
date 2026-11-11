ar =[1,3,4,5,5,6,7]


def binary_search(ar, x):
    print(ar)
    if len(ar)==1:
        return 0 if ar[0]==x else None
        
    mid = len(ar)//2
        # print(ar, mid, "love sisken ", ar[mid], x)
    if ar[mid]==x:
        return mid, "hi"
    elif ar[mid]<=x:
        return binary_search(ar[mid:], x)
    else:
        return binary_search(ar[:mid], x)



print(binary_search(ar, 2))
