class CollegeClass():
    def __init__(self, name, year, grade, subject):
        self.class_name = name
        self.year = year
        self.grade = grade
        self.subject = subject

    def edit_class(self):
        self.class_name = input("Enter class name: ")
        self.year = input("Enter year: ")
        self.grade = input("Enter grade earned: ")
        self.subject = input("Enter Subject")