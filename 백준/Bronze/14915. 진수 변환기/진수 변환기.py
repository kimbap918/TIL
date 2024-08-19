def decimal_converter(number, n):
    answer = ""
    temp = list("0123456789ABCDEF")
    
    if number == 0:
        answer = "0"
    else:
        while number:
            answer += temp[number % n]
            number //= n
            
    return answer[::-1]


if __name__ == "__main__":
    number, n = map(int, input().split())
    print(decimal_converter(number, n))