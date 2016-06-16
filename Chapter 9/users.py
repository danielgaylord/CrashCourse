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
