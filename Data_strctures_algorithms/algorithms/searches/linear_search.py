def linear(ar, x):
    for i in range(len(ar)):
        if x==ar[i]:
            return i
    return "not found"

ar =[1,3,4,5,2,5,6,7]
print(linear(ar, 1))