def same_numbers(N):
    return int(N // 10 == N % 10)


if __name__ == "__main__":
    N = int(input())
    print(same_numbers(N=N))