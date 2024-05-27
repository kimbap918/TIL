# 학생 정보를 입력 받는 class 를 만들어 보세요
# 이름, 국어점수, 수학점수를 입력받고 다음과 같이 출력 가능 

# 이름 : 오민엽
# 국어 : 80
# 수학 : 100
# 총점 : 180
# 평균 : 90

class Student:
    def set_info(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math
        
    def get_sum(self):
        return self.korean + self.math

    def get_average(self):
        return self.get_sum()/2

    def print_string(self):
        pass
