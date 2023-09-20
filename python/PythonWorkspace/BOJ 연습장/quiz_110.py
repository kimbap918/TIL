T = int(input())

def contest1(score):
    if score == 1:
        return 5000000
    elif 1 < score <= 3:
        return 3000000
    elif 3 < score <= 6:
        return 2000000
    elif 6 < score <= 10:
        return 500000
    elif 10 < score <= 15:
        return 300000
    elif 15 < score <= 21:
        return 100000
    else:
        return 0
def contest2(score):
    if score == 1:
        return 5120000
    elif 1 < score <= 3:
        return 2560000
    elif 3 < score <= 7:
        return 1280000
    elif 7 < score <= 15:
        return 640000
    elif 15 < score <= 31:
        return 320000
    else:
        return 0
for _ in range(T):
    first, second = map(int, input().split())
    print(contest1(first) + contest2(second))