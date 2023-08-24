def get_numbers_more_10(number_list):
    return [number for number in number_list if number >= 10]


def majestic_10(number_lists):
    answer_string_list = []
    for number_list in number_lists:
        answer_dict = {
            0: "zilch", 1: "double", 2: "double-double", 3: "triple-double"
        }

        more_10_num = get_numbers_more_10(
            number_list=number_list
        )
        
        more_10_num_len = len(more_10_num)

        answer = answer_dict[more_10_num_len]
        
        number_list = list(map(str, number_list))
        answer_string = f"{' '.join(number_list)}\n{answer}"
        answer_string_list.append(answer_string)
    
    return "\n\n".join(answer_string_list)


if __name__ == "__main__":
    number_lists = []
    for _ in range(int(input())):
        number_list = list(map(int, input().split()))
        number_lists.append(number_list)
        
    print(majestic_10(number_lists=number_lists))