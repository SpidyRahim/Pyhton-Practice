class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student with name : {self.name}, Class : {self.current_class}, id : {self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher with name : {self.name}, Subject : {self.subject}, id : {self.id}'


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teacher = []
        self.stdents = []

    def add_teacher(self, name, subject):
        id = len(self.teacher) + 101
        teacher = Teacher(name, subject, id)
        self.teacher.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            print(
                f'Enroll Unsuccessful!!! {fee} is not enough to enroll need {6500 - fee} more')
        else:
            id = len(self.stdents) + 1
            student = Student(name, 'C', id)
            self.stdents.append(student)
            print(f'{name} is enrolled with id : {id}, extra money : {fee - 6500}')
    
    def __repr__(self) -> str:
        print('Welcome To The School',self.name)
        print('-------------> Our Teachers <-------------')
        for teacher in self.teacher:
            print(teacher)
        print('-------------> Our Students <-------------')
        for student in self.stdents:
            print(student)
        return '-------------> End <-------------'
        

# # Rahim = Student('Rahim', 9, 1)
# # Sir = Teacher('Boss', 'Algorithm', 101)
# school = School('XYZ School')
# # print(Rahim)
# # print(Sir)
# school.add_teacher('X', 'DSA')
# school.add_teacher('Y', 'SA')
# school.add_teacher('Z', 'A')
# school.add_teacher('A', 'B')
# school.add_teacher('B', 'B')
# print(school.teacher)
phitron = School('Phitron')
phitron.enroll('Rahim', 5200)
phitron.enroll('Rahi', 52000)
phitron.enroll('Rah', 6500)

phitron.add_teacher('AJ','DS')
phitron.add_teacher('TC','Math')
phitron.add_teacher('RDJ','Algo')

print(phitron)