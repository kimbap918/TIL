import sys
n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))

my_sum = 0
for i in range(len(my_list)) :
    temp = 0
    for j in range(i,len(my_list)) :
        temp += abs(my_list[i] - my_list[j])
    temp = temp*2
    my_sum += temp

print(my_sum)
