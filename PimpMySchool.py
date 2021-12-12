from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def show_average_rating(self):
        average_rating = mean(sum(self.grades.values(), []))
        return average_rating
    def __str__(self):
        average_rating = self.show_average_rating()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        res = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {average_rating}\n'
            f'Курсы в процессе изучения: {courses_in_progress}\n'
            f'Завершенные курсы: {finished_courses}'
        )
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не студент")
            return
        else:
            self_average_rating = self.show_average_rating()
            other_average_rating = other.show_average_rating()
            return self_average_rating < other_average_rating
    def __le__(self, other):
        if not isinstance(other, Student):
            print("Не студент")
            return
        else:
            self_average_rating = self.show_average_rating()
            other_average_rating = other.show_average_rating()
            return self_average_rating <= other_average_rating
    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Не студент")
            return
        else:
            self_average_rating = self.show_average_rating()
            other_average_rating = other.show_average_rating()
            return self_average_rating == other_average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def show_average_rating(self):
        average_rating = mean(sum(self.grades.values(), []))
        return average_rating
    def __str__(self):
        average_rating = self.show_average_rating()
        res = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {average_rating}'
        )
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор")
            return
        else:
            self_average_rating = self.show_average_rating()
            other_average_rating = other.show_average_rating()
            return self_average_rating < other_average_rating
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор")
            return
        else:
            self_average_rating = self.show_average_rating()
            other_average_rating = other.show_average_rating()
            return self_average_rating <= other_average_rating
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор")
            return
        else:
            self_average_rating = self.show_average_rating()
            other_average_rating = other.show_average_rating()
            return self_average_rating == other_average_rating

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def rate_studies_for_students(students_list):
    study_vs_grade_dict = {}
    for student in students_list:
        for study in student.courses_in_progress:
            if study in study_vs_grade_dict:
                study_vs_grade_dict[study] += student.grades[study]
            else:
                study_vs_grade_dict[study] = student.grades[study]
    for study in study_vs_grade_dict:
        study_vs_grade_dict[study] = mean(study_vs_grade_dict[study])
        print(f'Средняя оценка за домашние задания по всем студентам за предмет "{study}" - {study_vs_grade_dict[study]}')

def rate_studies_for_lecturers(lecturers_list):
    study_vs_grade_dict = {}
    for lecturer in lecturers_list:
        for study in lecturer.courses_attached:
            if study in study_vs_grade_dict:
                study_vs_grade_dict[study] += lecturer.grades[study]
            else:
                study_vs_grade_dict[study] = lecturer.grades[study]
    for study in study_vs_grade_dict:
        study_vs_grade_dict[study] = mean(study_vs_grade_dict[study])
        print(f'Средняя оценка за за лекции всех лекторов в рамках курса "{study}" - {study_vs_grade_dict[study]}')

def main():
    students = []

    student1 = Student('Harry','Potter', 'M')
    student1.finished_courses = [ 'Astronomy', 'Charms' ]
    student1.courses_in_progress = [ 'Potions', 'Herbology' ]
    student1.grades = { 'Potions':[4, 5, 6] , 'Herbology':[5, 6, 8]}
    students.append(student1)

    student2 = Student('Hermione','Granger', 'F')
    student2.finished_courses = [ 'Astronomy', 'Charms', 'Arithmacy' ]
    student2.courses_in_progress = [ 'Potions', 'Herbology' ]
    student2.grades = { 'Potions':[8, 10, 10] , 'Herbology':[8, 10, 9]}
    students.append(student2)

    lecturers = []

    lecturer1 = Lecturer('Aurora', 'Sinistra')
    lecturer1.courses_attached = ['Astronomy']
    lecturer1.grades = { 'Astronomy':[8, 8, 7, 9, 10] }
    lecturers.append(lecturer1)

    lecturer2 = Lecturer('Filius', 'Flitwick')
    lecturer2.courses_attached = ['Charms']
    lecturer2.grades = { 'Charms':[10, 10, 8, 9, 10] }
    lecturers.append(lecturer2)

    reviewer1 = Reviewer('Horace', 'Slughorn')
    reviewer1.courses_attached = ['Potions']

    reviewer2 = Reviewer('Pomona', 'Sprout')
    reviewer2.courses_attached = ['Herbology']

    student1.rate_lecturer(lecturer1, 'Astronomy', 10)
    student2.rate_lecturer(lecturer2, 'Charms', 9)

    reviewer1.rate_hw(student1, 'Potions', 5)
    reviewer2.rate_hw(student2, 'Herbology', 10)

    if student1 > student2:
        print(f'Студент {student1.name} {student1.surname} учится лучше, чем {student2.name} {student2.name}.')
    elif student1 < student2:
        print(f'Студент {student1.name} {student1.surname} учится хуже, чем {student2.name} {student2.name}.')
    elif student1 == student2:
        print(f'Студент {student1.name} {student1.surname} учится так же, как {student2.name} {student2.name}.')

    if lecturer1 > lecturer2:
        print(f'Лектор {lecturer1.name} {lecturer1.surname} читает лекции лучше, чем {lecturer2.name} {lecturer2.name}.')
    elif lecturer1 < lecturer2:
        print(f'Лектор {lecturer1.name} {lecturer1.surname} читает лекции хуже, чем {lecturer2.name} {lecturer2.name}.')
    elif lecturer1 == lecturer2:
        print(f'Лектор {lecturer1.name} {lecturer1.surname} читает лекции так же, как {lecturer2.name} {lecturer2.name}.')

    rate_studies_for_students(students)
    rate_studies_for_lecturers(lecturers)

main()
