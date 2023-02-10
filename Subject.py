import uuid
from Meeting import Meeting


class Subject:
    def __init__(self, name, cost, prerequisite_classes, min_grade):
        self.name = name
        self.cost = cost
        self.prerequisites = prerequisite_classes
        self.min_grade = min_grade
        self.meetings = []
        self.subject_id = uuid.uuid1()

    def check_pre_requisites(self):
        pass

    def edit_name(self, new_name):
        self.name = new_name

    def edit_cost(self, new_cost):
        self.cost = new_cost

    def edit_prereq(self, new_prereq):
        self.prerequisites = new_prereq

    def edit_min_grade(self, new_min_grade):
        self.min_grade = new_min_grade

    def meeting_dashboard(self):
        menu = """
        MEETING DASHBOARD
        1)Add Meeting
        2)Edit Meetings
        3)Exit
        """
        choice = None
        while choice != "3":
            choice = input(menu)
            if choice == "1":
                self.add_meeting()
            elif choice == "2":
                self.edit_meetings()

    def add_meeting(self):
        meeting1 = Meeting(date=input("Enter Meeting Dates: "), room=input("Enter Meeting Room: "))
        self.meetings.append(meeting1)
        print(meeting1.meeting_id)

    def edit_meetings(self):
        meeting_uuid = input("Enter meeting uuid: ")
        for meeting in self.meetings:
            if meeting_uuid == str(meeting.meeting_id):
                meet_menu = """
                EDIT MEET MENU
                1)Edit Meeting Date
                2)Edit Meeting Room
                3:Exit
                """
                meet_choice = None
                while meet_choice != "3":
                    meet_choice = input(meet_menu)
                    if meet_choice == "1":
                        meeting.edit_date(input("Enter new meeting dates: "))
                    elif meet_choice == "2":
                        meeting.edit_room(input("Enter new meeting room: "))
