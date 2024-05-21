
def city():
    city_list = []
    
    while True:
        print("1. 도시를 추가")
        print("2. 추가 완료")
        print("3. 종료")
        try:
            name = int(input("값을 입력하세요 :"))
        except ValueError:
            print("숫자를 입력하세요")
            continue

        if name == 1:
            city_name = input("도시를 영어로 입력하세요: ")
            city_list.append(city_name)
        elif name == 2:
            print(city_list)
            print("종료")
            exit(0)
        elif name == 3:
            exit(0)

city()
