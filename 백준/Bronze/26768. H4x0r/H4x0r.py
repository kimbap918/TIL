def h4x0r(string):
    replace_dict = {
        "a": "4", "e": "3", "i": "1", "o": "0", "s": "5"
    }
    
    return "".join([replace_dict[word] if word in replace_dict else word for word in list(string)])

if __name__ == "__main__":
    string = input()
    
    print(h4x0r(string=string))