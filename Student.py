from User import User


class Student(User):
    def __init__(self):
        self.__college_number = None
        self.__study_year = None
        self.past_classes = []
        self.current_classes = []
        self.schedule = []
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



