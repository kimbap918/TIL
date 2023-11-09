for _ in range(int(input())):
    n = int(input())
    if n < 3:
        for i in range(n):
            print('#'*n)
        print()
    else:
        print('#'*n)
        for i in range(n-2):
            print('#' + 'J'*(n-2) + '#')
        print('#'*n, '\n')