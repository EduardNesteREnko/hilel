
class GroupFullException(Exception):
    def __init__(self, message="Group already have 10 students, it`s not possible to add extra"):
        super().__init__(message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o.'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()}, Record book: {self.record_book}'

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(st) for st in self.group)
        return f'Group Number: {self.number}\n{all_students}'

gr = Group('PD1')


for i in range(10):
    st = Student('Male', 20 + i, f'Name{i}', f'Lastname{i}', f'ID{i}')
    gr.add_student(st)

 
try:
    extra_student = Student('Female', 21, 'Extra', 'Student', 'ID11')
    gr.add_student(extra_student)
except GroupFullException as e:
    print(f"Помилка: {e}")
