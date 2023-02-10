class Course():
    def __init__(self, name, faculty):
        self.__name = name
        self.__faculty = faculty

    def get_name(self):
        return self.__name

    def get_faculty(self):
        return self.__faculty
