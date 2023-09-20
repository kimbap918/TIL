def divide_the_cash(team_member_numbers, money):
    total_team_num = sum(team_member_numbers)
    
    money_for_each_member = money // total_team_num
    
    return [member_num * money_for_each_member for member_num in team_member_numbers]


def print_answer(answer):
    for ans in answer:
        print(ans)


if __name__ == "__main__":
    team_member_numbers = []
    N, money = map(int, input().split())
    
    for _ in range(N):
        member_num = int(input())
        team_member_numbers.append(member_num)
    
    answer = divide_the_cash(
        team_member_numbers=team_member_numbers, money=money
    )
    
    print_answer(answer=answer)