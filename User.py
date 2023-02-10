class User:
    def __init__(self):
        self.__first_name = None
        self.__last_name = None
        self.__account = None
        self.__password = None
        self.__address = None
        self.__telephone = None
        self.__email = None
        self.__is_logged_in = False

    def sign_in(self):
        account = input("Please Enter Your Username: ")
        password = input("Please Enter Your Password: ")
        if self.__account == account and self.__password == password:
            print("Logged In")
            self.__is_logged_in = True
            return True
        else:
            print("Not Logged In")
            return False

    def edit_personal_info(self):
        if self.__is_logged_in == True:
            menu = """
            Choose Which You Would Like To Edit
            
            1)Address
            2)Phone Number
            3)Email
            4)Exit
            :
            """
            choice = None
            while choice != "4":
                choice = input(menu)
                if choice == "1":
                    self.__address = input("Enter New Address: ")
                elif choice == "2":
                    self.__telephone = input("Enter New Phone Number: ")
                elif choice == "3":
                    self.__email = input("Please Enter New Email: ")
                print("Edited Successfully")
        else:
            print("Please Log in: ")
            self.sign_in()

    def register(self):
        self.__account = input("Please enter a username: ")
        self.__first_name = input("Please enter your first name: ")
        self.__last_name = input("Please enter your last name: ")
        self.__password = input("Please enter your password: ")
        self.__address = input("Please enter your address: ")
        self.__telephone = input("Please enter your phone number: ")
        self.__email = input("Please enter your email: ")
        print("Successfully Registered")

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_account(self):
        return self.__account

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_telephone(self):
        return self.__telephone

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return f"""
Account Info:
Username: {self.__account}
First Name: {self.__first_name}
Last Name: {self.__last_name}
Password: {self.__password}
Address: {self.__address}
Phone Number: {self.__telephone}
Email: {self.__email}
"""

