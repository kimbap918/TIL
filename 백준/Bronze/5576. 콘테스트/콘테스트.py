w_list = []
k_list = []
w_sum, k_sum = 0, 0

for _ in range(10):
    W = int(input())
    w_list.append(W)

for _ in range(10):
    K = int(input())
    k_list.append(K)

w_list.sort(reverse=True)
k_list.sort(reverse=True)

for i in range(3):
    w_sum += w_list[i]
    k_sum += k_list[i]

print("{} {}".format(w_sum, k_sum))
