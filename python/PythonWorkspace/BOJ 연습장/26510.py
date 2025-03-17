N = list(map(int, input().split()))

for i in range(len(N)): # N번 반복
    num = N[i]
    
    for j in range(num, 0, -1):
        if j == 1:
            print(" " * (num-1) + "*")
        else:
            print(" " * (num-j) + "*" + " " * (2*j-3)+ "*")

        # print("*" * N[i])


# N = 2

# * * 3
#  * 2
# *   * 5
#  * * 4
#   * 3
# *     * 7
#  *   * 6
#   * * 5
#    * 4


# 2 3 4 5 6 7

# (1) (3,1) (5, 3, 1) (7, 5, 3, 1) (9, 7, 5, 3, 1) (11, 9, 7, 5, 3, 1)
