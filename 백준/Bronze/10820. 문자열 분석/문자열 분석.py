while True :
    try :
        text_lst = list(input())
        lower , upper, num, blank = 0,0,0,0
        for i in range(len(text_lst)) :
            if text_lst[i] == " " :
                blank += 1
            elif 65 <= ord(text_lst[i]) <= 90 :
                upper += 1
            elif 97 <= ord(text_lst[i]) <= 122 :
                lower += 1
            else :
                num += 1
        print(lower,upper,num,blank)
    except EOFError :
        break