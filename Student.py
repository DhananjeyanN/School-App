from CollegeClass import CollegeClass
from User import User
from datetime import datetime
import uuid


class Student(User):
    def __init__(self):
        self.__college_number = None
        self.__study_year = None
        self.past_classes = []
        self.current_classes = []
        self.schedule = []
        self.register_date = None

    def enroll(self, subject):
        if self.check_prerequisite(subject):
            self.current_classes.append(subject)
            print("Course Added Successfully")
        else:
            print("Sorry requirements not fulfilled")

    def meeting_register(self, meeting, subject):
        for meet in subject.meetings:
            if meet.date == meeting.date and meet.room == meeting.room:
                self.schedule.append(meet)
                print("Registered")
            else:
                print("Incorrect Meeting")

    def view_data(self, object):
        pass

    def is_allowed(self, subject):
        pass

    def check_prerequisite(self, subject):
        for college_class in self.past_classes:
            if college_class.subject.name == subject.name and college_class.grade >= subject.min_grade:
                return True

        return False

    def register_student(self):
        self.register()
        self.register_date = datetime.strptime(input("Please enter today's date in this format mm/dd/yyyy: "),
                                               "%d/%m/%Y")
        self.__study_year = datetime.today().year
        self.__college_number = uuid.uuid1()
        print(self.__college_number)

    def get_uuid(self):
        return self.__college_number

    def edit_student(self):
        menu = """
        1) Edit Past Classes
        2) Edit Current Classes
        3) Edit Study Year
        4) Edit Register Date
        5) Edit First Name
        6) Edit Last Name
        7) Edit Account Name
        8) Edit Password
        9) Edit Address
        10) Edit Phone Number
        11) Edit Email
        12) Exit
        """
        choice = None
        while choice != "12":
            choice = input(menu)
            if choice == "1":
                past_class = CollegeClass(input("Enter class name: "), input("Enter year: "), input("Enter grade: "),
                                          input("Enter subject: "))
                self.past_classes.append(past_class)
            elif choice == "2":
                past_class = CollegeClass(input("Enter class name: "), input("Enter year: "), input("Enter grade: "),
                                          input("Enter subject: "))
                self.current_classes.append(past_class)
            elif choice == "3":
                self.__study_year = input("Enter new study year: ")
            elif choice == "4":
                self.register_date = input("Enter students new register date: ")
            elif choice == "5":
                super().set_first_name(input("Enter new first name: "))
            elif choice == "6":
                super().set_last_name(input("Enter new last name: "))
            elif choice == "7":
                super().__account = input("Enter new username: ")
            elif choice == "8":
                super().set_password(input("Enter new password"))
            elif choice == "9":
                super().set_address(input("Enter new address: "))
            elif choice == "10":
                super().set_telephone(input("Enter new phone_number: "))
            elif choice == "11":
                super().set_email(input("Enter new email: "))
