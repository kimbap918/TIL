def point_study(N):
    print("int a;")
    
    for idx in range(1, N + 1):
        before_and_string = f"ptr{idx-1 if idx-1 > 1 else ''};" if idx > 1 else "a;"
        print(f"int {'*' * idx}ptr{idx if idx > 1 else ''} = &{before_and_string}")
              
if __name__ == "__main__":
    N = int(input())
    point_study(N=N)