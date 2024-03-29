li = [int(input()) for _ in range(5)]
X = li[4]*li[0]
Y = li[1] + li[3]*max(0, li[4]-li[2])
print(min(X, Y))