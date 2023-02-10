class Exam():
    def __init__(self, date, semester):
        self.__date  = date
        self.__semester = semester

    def get_date(self):
        return self.__date

    def get_semester(self):
        return self.__semester