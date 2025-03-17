import random

array = [i for i in range(0, 10)]
random.shuffle(array)

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
