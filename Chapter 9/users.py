class User:

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Gender: " + self.gender)
        print("Age: " + str(self.age))

    def greet_user(self):
        print("Hello, " + self.first_name + ", welcome back!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


u1 = User("Dan", "Gaylord", "M", 29)
u1.describe_user()
u1.greet_user()
print()

u2 = User("Jim", "Gaylord", "M", 27)
u2.describe_user()
u2.greet_user()
print()

u3 = User("Shien", "Zou", "F", 27)
u3.describe_user()
u3.greet_user()
u3.increment_login_attempts()
u3.increment_login_attempts()
print(str(u3.login_attempts))
u3.reset_login_attempts()
print(str(u3.login_attempts))
