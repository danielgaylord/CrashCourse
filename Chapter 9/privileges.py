class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("The admin can:")
        for privy in self.privileges:
            print("\t" + privy)
