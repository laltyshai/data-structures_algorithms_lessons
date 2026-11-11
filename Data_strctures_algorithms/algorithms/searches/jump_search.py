ar =[i for i in range(100)]


def jump(ar, x , jump):
    a=[]
    for i in range(0,len(ar),jump):
        if ar[i]==x:
            return i
        elif ar[i]> x:
            for j in range(a, i):
                if ar[j] ==x:
                    return j
            return None
        else:
            a=i
    return None
import time

start = time.time()


print(jump(ar, 7, 20))


time.sleep(1)
end = time.time()
print(f"Total runtime of the program is {end - start} seconds")
