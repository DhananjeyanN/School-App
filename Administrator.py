from Student import Student
from Subject import Subject
from Teacher import Teacher
from User import User


class Administrator(User):
    def __init__(self):
        super().__init__()
        self.students = []
        self.teachers = []
        self.subjects = []

    def edit_data(self, obj, type):
        self.edit_dashboard()

    def time_tabling(self, schedule, rooms):
        pass

    def edit_dashboard(self):
        menu = """
        EDIT DASHBOARD
        1) Student
        2) Teacher
        3) Subject
        4) Exit
        """

        choice = None
        while choice != "4":
            choice = input(menu)
            if choice == "1":
                self.student_dashboard()
            elif choice == "2":
                self.teacher_dashboard()
            elif choice == "3":
                self.subject_dashboard()

    def student_dashboard(self):
        menu = """
        STUDENT DASHBOARD
        1) Add Student
        2) Edit Student
        3) Remove Student
        4) Exit
        """
        choice = None
        while choice != "4":
            choice = input(menu)
            if choice == "1":
                student = Student()
                student.register_student()
                self.students.append(student)
                print("Added student successfully")
            elif choice == "2":
                uuid = input("Enter student unique id: ")
                for student in self.students:
                    if uuid == str(student.get_uuid()):
                        student.edit_student()
            elif choice == "3":
                uuid = input("Enter student unique id: ")
                for student in self.students:
                    if uuid == str(student.get_uuid()):
                        self.students.remove(student)

    def teacher_dashboard(self):
        menu = """
        TEACHER DASHBOARD
        1) Add Teacher
        2) Edit Teacher
        3) Remove Teacher
        4) Exit
        """
        choice = None
        while choice != "4":
            choice = input(menu)
            if choice == "1":
                teacher = Teacher()
                teacher.register_teacher()
                print("Added Teacher successfully")
            elif choice == "2":
                uuid = input("Enter teacher unique id: ")
                for teacher in self.teachers:
                    if uuid == str(teacher.get_uuid()):
                        teacher.edit_teacher()
            elif choice == "3":
                uuid = input("Enter teacher unique id: ")
                for teacher in self.teachers:
                    if uuid == str(teacher.get_uuid()):
                        self.teachers.remove(teacher)

    def subject_dashboard(self):
        m = """
        SUBJECT DASHBOARD
        1)Add Subject
        2)Edit Subject
        3)Exit
        """
        choice2 = None
        while choice2 != "3":
            choice2 = input(m)
            if choice2 == "1":
                subject1 = Subject(name=input("Enter Subject Name: "), cost=input("Enter Subjects cost: "),
                                   prerequisite_classes=input("Enter Subjects Prerequisite Classes: "),
                                   min_grade=input("Enter Subjects minimum grade: "))
                self.subjects.append(subject1)
                print(subject1.subject_id)
            elif choice2 == "2":
                self.edit_subject_dashboard(input("Enter Subject ID: "))

    def edit_subject_dashboard(self, subject_id):
        for subject in self.subjects:
            if str(subject.subject_id) == subject_id:
                menu = """
                SUBJECT EDIT DASHBOARD
                1) Edit Subject Name
                2) Edit Subject Cost
                3) Edit Subject Prerequisite Classes
                4) Edit Subject Minimum Grade
                5) Edit Subject Meetings
                6) Exit
                """
                choice = None

                while choice != "6":
                    choice = input(menu)
                    if choice == "1":
                        subject.edit_name(input("Enter new subject name: "))
                    elif choice == "2":
                        subject.edit_cost(input("Enter new subject cost: "))
                    elif choice == "3":
                        subject.edit_prereq(input("Enter new prerequisites: "))
                    elif choice == "4":
                        subject.edit_min_grade(input("Enter new minimum grade for subject: "))
                    elif choice == "5":
                        subject.meeting_dashboard()

    def register(self):
        super().register()


admin1 = Administrator()
admin1.edit_dashboard()
