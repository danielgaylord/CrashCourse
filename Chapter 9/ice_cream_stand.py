from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, 'ice cream')
        self.flavors = flavors

    def show_flavors(self):
        print("Our flavors include:")
        for flavor in self.flavors:
            print("\t" + flavor.title())

