from User import User
import uuid

class Teacher(User):
    def __init__(self):
        super().__init__()
        self.meetings = []
        self.__uuid = None
    # def manipulate_meeting(self, meeting, subject):
    #     for meet in subject.meetings:
    #         if meet.date == meeting.date and meet.room == meeting.room:
    #             choice = input("1)Remove \n 2)Edit")
    #             if choice == "1":
    #                 return False
    #             elif choice == "2":


    def get_uuid(self):
        return self.__uuid

    def register_teacher(self):
        self.uuid = uuid.uuid1()
        super().register()

    def edit_teacher(self):
        menu = """
        TEACHER EDIT DASHBOARD
        1) Edit First Name
        2) Edit Last Name
        3) Edit Account Name
        4) Edit Password
        5) Edit Address
        6) Edit Phone Number
        7) Edit Email
        8) Edit Meetings
        9) Exit
        """
        choice = None
        while choice != "9":
            choice = input(menu)

            if choice == "1":
                super().set_first_name(input("Enter new first name: "))
            elif choice == "2":
                super().set_last_name(input("Enter new last name: "))
            elif choice == "3":
                super().__account = input("Enter new username: ")
            elif choice == "4":
                super().set_password(input("Enter new password"))
            elif choice == "5":
                super().set_address(input("Enter new address: "))
            elif choice == "6":
                super().set_telephone(input("Enter new phone_number: "))
            elif choice == "7":
                super().set_email(input("Enter new email: "))
            elif choice == "8":
                meeting_id = input("Enter Unique id for meeting: ")
                for meeting in self.meetings:
                    if meeting.meeting_id == meeting_id:
                        meet_menu = """
                        MEET MENU
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




