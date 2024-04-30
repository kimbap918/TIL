def golbange_print_rotate_ㄹ(N):
    answer = ['' for _ in range(N * 5)]
    
    for idx in range(N*5):
        if idx < N:
            answer[idx] = f"{'@' * (N * 3)}{' ' * N}{'@' * N}"
        elif N <= idx < N * 5 - N:
            answer[idx] = f"{'@' * N}{' ' * N}{'@' * N}{' ' * N}{'@' * N}"
        else:
            answer[idx] = f"{'@' * (N)}{' ' * N}{'@' * N * 3}"
            
        
    return "\n".join(answer)


if __name__ == "__main__":
    N = int(input())
    
    print(golbange_print_rotate_ㄹ(N=N))