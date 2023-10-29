class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        self.grades_average_hw = float()
        
    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'
        
    def avg_rating(self):
        grades_count = 0
        for grade in self.grades_student:
            grades_count += len(self.grades_student[grade])
        avg_rating = sum(map(sum, self.grades_student.values())) / grades_count
        return str(avg_rating)
        
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg_rating()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.avg_rating() > other.avg_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []       


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lecturer = {}
        self.grades_average_lecture = []

    def __str__(self):
        grades_count = 0
        for grade in self.grades_lecturer:
            grades_count += len(self.grades_lecturer[grade])
        self.avg_rating = sum(map(sum, self.grades_lecturer.values())) / grades_count
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg_rating}\n")
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.avg_rating > other.avg_rating

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")
    


# студенты
student_1 = Student('Ruoy', 'Eman')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ryan', 'Gosling')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

# лекторы
lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Jason', 'Statham')
lecturer_2.courses_attached += ['Python']

# проверяющие

reviewer_1 = Reviewer('Benedict', 'Cumberbatch')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

# оценки студентов 
reviewer_1.rate_hw_student(student_1, 'Python', 10)
reviewer_1.rate_hw_student(student_1, 'Python', 9)
reviewer_1.rate_hw_student(student_1, 'Python', 8)
reviewer_1.rate_hw_student(student_1, 'Git', 7)

reviewer_1.rate_hw_student(student_2, 'Python', 9)
reviewer_1.rate_hw_student(student_2, 'Python', 9)
reviewer_1.rate_hw_student(student_2, 'Python', 9)
reviewer_1.rate_hw_student(student_2, 'Git', 10)

# оценки лекторов
student_1.rate_hw_lecturer(lecturer_1, 'Python', 7)
student_1.rate_hw_lecturer(lecturer_1, 'Python', 6)
student_1.rate_hw_lecturer(lecturer_1, 'Python', 3)

student_2.rate_hw_lecturer(lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(lecturer_2, 'Python', 10)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

def students_rate(students_list, course_name):
    some_list = []
    summ = 0
    countt = 0
    for student_hw in students_list:
        for key, value in student_hw.grades_student.items():
          if key == course_name:
            some_list.append(value)
    for i in some_list:
        for n in i:
            summ+=n
            countt+=1
    avg_rating_all = summ / countt
    return avg_rating_all

def lecturer_rate(lecturers_list, course_name):
    some_list = []
    summ = 0
    countt = 0
    for lecturer_lt in lecturers_list:
        for key, value in lecturer_lt.grades_lecturer.items():
          if key == course_name:
            some_list.append(value)
    for i in some_list:
        for n in i:
            summ+=n
            countt+=1
    avg_rating_all = summ / countt
    return avg_rating_all


print()
print()
print(f'Проверяющий:\n\n{reviewer_1}\n\n')

print(f'Студенты:\n\n{student_1}\n\n{student_2}\n\n')

print(f'Лекторы:\n\n{lecturer_1}\n\n{lecturer_2}\n\n')

print(student_1 < student_2)

if (student_1 < student_2) == True:
    print(f'Лучший студент {student_2.name} {student_2.surname}')
else:
    print(f'Лучший студент {student_1.name} {student_1.surname}')

if (lecturer_1 < lecturer_2) == True:
    print(f'Лучший лектор {lecturer_2.name} {lecturer_2.surname}')
else:
    print(f'Лучший лектор {lecturer_1.name} {lecturer_1.surname}')


print(f"Средняя оценка всех студентов по курсу {'Python'}: {students_rate(student_list, 'Python')}")
print()

print(f"Средняя оценка всех лекторов по курсу {'Python'}: {lecturer_rate(lecturer_list, 'Python')}")
print()



