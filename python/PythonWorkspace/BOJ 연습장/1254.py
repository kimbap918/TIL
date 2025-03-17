#abab
#ababa


#abacaba
#abacaba 

#qwerty
#qwertytrewq



#abdfhdyrbdbsdfghjkllkjhgfds  
#abdfhdyrbdbsdfghjkllkjhgfdsbdbrydhfdba

# 1. 팰린드롬인지 확인
# 2. 팰린드롬이 아니라면 기준점 파악
# 3. 기준점에서 한 글자씩 붙혀서 팰린드롬이 완성되는지 확인
# 4. 길이 측정


def is_pal(words):
    return words == words[::-1]

def pal_maker(words):
    if is_pal(words):
        return len(words)

    for i in range(len(words)): # abab 
        # 0 1 2 3

        extend = words + words[:i][::-1]
        # print("words[:i][::-1] : "+words[:i][::-1])
        # print("words+words[:i][::-1] : "+words+words[:i][::-1])

        if is_pal(extend):
            return len(extend)

word = input()
print(pal_maker(word))
    

