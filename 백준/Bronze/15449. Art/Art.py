from itertools import combinations
from math import sqrt

any_sticks = list(map(int, input().split()))
arr  = []

def get_area(arr):
    s = sum(arr)/2
    t = s*(s-arr[0])*(s-arr[1])*(s-arr[2])
    if t < 1: return
    return sqrt(t)

for i, sticks in enumerate(list(combinations(any_sticks, 3))):
    area = get_area(sticks)
    if area is not None: 
        arr.append(area)
print(len(set(arr)))
