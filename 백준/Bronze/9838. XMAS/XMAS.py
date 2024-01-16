def XMAS(gift_list):
    check_dict = {}
    for idx, gift in enumerate(gift_list, start=1):
        check_dict[gift] = idx

    items = [item[1] for item in sorted(check_dict.items(), key=lambda x: x[0])]
    
    return items
    
if __name__ == "__main__":
    gift_list = []
    for _ in range(int(input())):
        gift_list.append(int(input()))
        
    check_list = XMAS(gift_list)
    
    for check in check_list:
        print(check)