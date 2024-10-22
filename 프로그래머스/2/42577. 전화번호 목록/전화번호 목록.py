def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        test = phone_book[i+1]
        if phone_book[i] in phone_book[i+1] and test[:len(phone_book[i])] == phone_book[i]:
            answer = False
            break
        else:
            answer = True
    return answer