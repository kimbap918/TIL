class BusinessCard:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def print_card(self):
        print("="*30)
        print(f"Name : {self.name}")
        print(f"E-mail : {self.email}")
        print(f"Address : {self.address}")
        print("="*30)

# 클래스 사용 예시
name_1 = input("이름을 입력하세요 : ")
email_1 = input("메일을 입력하세요 : ")
add_1 = input("주소를 입력하세요 : ")

card = BusinessCard(name_1, email_1, add_1)
card.print_card()

