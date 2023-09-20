def gum_gum_for_jay_jay():
    answer = 0
    
    while True:
        try:
            gum_gum = input()
            answer += 1
        except EOFError:
            break
    
    return answer


if __name__ == "__main__":
    print(gum_gum_for_jay_jay())