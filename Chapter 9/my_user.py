from users import User

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
