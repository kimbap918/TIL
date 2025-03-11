
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
    

