class Student:
    def __init__(self, name, **subjects):
        self.name = name
        # print("응애에요")
        self.subjects = subjects

    def add_score(self, subject, score):
        self.subjects[subject] = score

    def get_sum(self):
        return sum(self.subjects.values())

    def get_average(self):
        return self.get_sum()/len(self.subjects)

    def print_string(self):
        subject_socre = "\n".join([f"{subject} : {score}" for subject, score in self.subjects.items()])
        print(f'''
이름 : {self.name}
{subject_socre}
총점 : {self.get_sum()}
평균 : {self.get_average()}
        ''')