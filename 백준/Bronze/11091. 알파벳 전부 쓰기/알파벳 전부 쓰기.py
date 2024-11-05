import re

def use_all_alphabet(string, alphabets):
    is_pangram = "pangram"
    
    string = re.sub(r"[^a-z]", '', string.lower())
    
    string = set(string)
    not_uesd_alphabet = alphabets - string
    
    if not_uesd_alphabet != set():
        not_uesd_alphabet = sorted(list(not_uesd_alphabet))
        
        is_pangram = f"missing {''.join(not_uesd_alphabet)}"
        
    return is_pangram

if __name__ == "__main__":
    alphabets = set([chr(i) for i in range(97, 123)])

    for _ in range(int(input())):
        string = input()
        print(use_all_alphabet(string, alphabets))