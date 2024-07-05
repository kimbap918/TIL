if __name__ == '__main__':
    equation = ''
    n = int(input())
    for _ in range(n + n - 1):
        equation += input()
    equation = equation.replace('/', '//')
    print(eval(equation))