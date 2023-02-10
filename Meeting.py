import uuid
class Meeting:
    def __init__(self, date, room):
        self.date = date
        self.room = room
        self.meeting_id = uuid.uuid1()

    def __str__(self):
        return f"Date: {self.date} | Room: {self.room}"

    def edit_date(self, new_date):
        self.date = new_date

    def edit_room(self, new_room):
        self.room = new_room