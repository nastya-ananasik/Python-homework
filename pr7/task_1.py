class UserValidator:
    @staticmethod
    def validate_email(email):
        if "@" not in email:
            raise ValueError("Некорректный email")

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.is_active = True

    @classmethod
    def create_user(cls, user_id: int, name: str, email: str):
        UserValidator.validate_email(email)
        return cls(user_id, name, email)

    def update_profile(self, new_name: str = None, new_email: str = None):
        if new_email:
            UserValidator.validate_email(new_email)
            self.email = new_email
        if new_name:
            self.name = new_name
        print(f"User {self.id} updated.")

    def delete_user(self):
        self.is_active = False
        print(f"User {self.id} deleted (soft).")

user = User.create_user(1, "Alex", "alex@example.com")
user.update_profile(new_name="Alexander")
user.delete_user()
