def golbange_print_ㅈ(N):
    answer = ['' for _ in range(N * 5)]
    
    for idx in range(N*5):
        if 2 * N - 1 < idx < 2 * N + N:
            answer[idx] = "@" * (N * 3)
        elif idx < 2 * N:
            answer[idx] = f"{'@' * N}{((3-(idx // N)) * N) * ' '}{'@' * (N)}"
        else:
            answer[idx] = f"{'@' * N}{((idx // N) * N - N ) * ' '}{'@' * (N)}"
        
    return "\n".join(answer)


if __name__ == "__main__":
    N = int(input())
    
    print(golbange_print_ㅈ(N=N))