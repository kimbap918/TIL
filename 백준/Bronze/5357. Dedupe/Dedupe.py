def dedupe(dup_string):
    dedupe_string = [dup_string[0]]
    
    for word in dup_string[1:]:
        if word != dedupe_string[-1]:
            dedupe_string.append(word)
            
    return "".join(dedupe_string)


if __name__ =="__main__":
    for _ in range(int(input())):
        dup_string = input()
        
        print(dedupe(dup_string=dup_string))