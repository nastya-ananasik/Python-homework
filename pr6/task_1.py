class User:
    def __init__(self):
        self.__name = ""
        self.__email = ""
        self.__password = ""

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name):
        if name and isinstance(name, str):
            self.__name = name

    def set_email(self, email):
        if email and "@" in email:
            self.__email = email

    def set_password(self, password):
        if password and len(password) >= 8:
            self.__password = password

user = User()

user.set_name("Анастасія")
user.set_email("ananasik@gmail.com")
user.set_password("123456Seven")

print(f"Ім'я: {user.get_name()}")
print(f"Email: {user.get_email()}")
print(f"Пароль: {user.get_password()}")
