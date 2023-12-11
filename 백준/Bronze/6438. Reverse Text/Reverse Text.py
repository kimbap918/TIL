def reverse_text(text):
    split_text = text.split()
    
    split_text = [text[::-1] for text in split_text][::-1]
    
    return " ".join(split_text)


if __name__ == "__main__":
    for _ in range(int(input())):
        text = input()
        print(reverse_text(text=text))