def absolutely(value1, value2):
    return round(abs(value1-value2), 1)


if __name__ == "__main__":
    for _ in range(int(input())):
        value1, value2 = map(float, input().split())
        
        print(absolutely(value1=value1, value2=value2))