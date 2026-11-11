def interpolation(ar, x):
    # ar must be sorted
    low = 0
    high = len(ar) - 1

    while low <= high and ar[low] <= x <= ar[high]:
        # all values in this range are equal -> avoid dividing by zero
        if ar[high] == ar[low]:
            return low if ar[low] == x else None

        # guess where x should be, assuming values are spread evenly
        pos = low + (x - ar[low]) * (high - low) // (ar[high] - ar[low])

        if ar[pos] == x:
            return pos
        elif ar[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return None


ar = [1, 3, 4, 5, 5, 6, 7, 10, 12, 15]

print(interpolation(ar, 1))   # 0
print(interpolation(ar, 7))   # 6
print(interpolation(ar, 15))  # 9
print(interpolation(ar, 8))   # None
print(interpolation([], 3))   # None
