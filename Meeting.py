class Meeting:
    def __init__(self, date, room):
        self.date = date
        self.room = room

    def __str__(self):
        return f"Date: {self.date} | Room: {self.room}"