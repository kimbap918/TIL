import sys

input = sys.stdin.readline

def dolmen(a: int, b: int):                
    return (a + b) * (a + b - 1) * (a + b) // 2
    

def archaeologist_yerin(a, b):
    return dolmen(a=a, b=b)


if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = map(int, input().split())
        
        print(archaeologist_yerin(a=a, b=b))