
black = '\u2605'
white = '\u2606'

N = int(input("별을 원하는 개수만큼 만들어봐요 : "))

# ★
# ★★
# ★★★
# ★★★★
# ★★★★★

# for i in range(1, N+1):
#     print(black*i)
    

# ★★★★★
# ★★★★
# ★★★
# ★★
# ★

# for i in range(N, 0, -1):
#     print(black*i)


# ☆☆☆☆★
# ☆☆☆★★
# ☆☆★★★
# ☆★★★★
# ★★★★★

# for i in range(N, 0, -1):
#     print(white*(i-1) + black*(N+1-i))


# for i in range(N, 0, -1):
#     print(' '*((N-1)-(N-i)) + black*(N+1-i) )

#     ★
#    ★★
#   ★★★
#  ★★★★
# ★★★★★