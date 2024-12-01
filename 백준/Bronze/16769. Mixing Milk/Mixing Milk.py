c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

capacity = [c1, c2, c3]
milk = [m1, m2, m3]

for i in range(100):
    a = milk[i % 3]
    b = milk[(i+1) % 3]
    if milk[i % 3] + milk[(i+1) % 3] > capacity[(i+1) % 3]:

        milk[i % 3] = a + b - capacity[(i+1) % 3]

        milk[(i + 1) % 3] = capacity[(i+1) % 3]

    else:
        milk[i % 3] = 0

        milk[(i + 1) % 3] = a + b

for i in range(3):
    print(milk[i])