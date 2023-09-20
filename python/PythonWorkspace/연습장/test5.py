import random

computer = random.randint(1, 100)
cnt = 0 

while True:
    user = input()
    cnt += 1

    if not user.isdigit() or int(user) < 1 or int(user) > 100:
        print("1에서 100사이의 정수를 입력하세요")
        cnt -= 1
        print("남은 횟수 : "+str(10-cnt))
        continue 

    user = int(user)
    
    if cnt == 10:
        print("실패")
        break
    if computer > user:
        print("up")
        print("남은 횟수 : "+str(10-cnt))
    elif computer < user:
        print("down")
        print("남은 횟수 : "+str(10-cnt))
    else:
        print("정답")
        break
