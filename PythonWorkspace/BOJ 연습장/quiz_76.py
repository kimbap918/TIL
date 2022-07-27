A = list(map(int, input().split()))
kong_list = [i % 8 for i in A]
if kong_list == [1,2,3,4,5,6,7,0]:
    print('ascending')
elif kong_list == [0,7,6,5,4,3,2,1]:
    print('descending')
else:
    print('mixed')