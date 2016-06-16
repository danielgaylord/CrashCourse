class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name.title() + ", we serve " +
              self.cuisine_type.title() + " food every day!")

    def open_restaurant(self):
        print("WE ARE OPEN!")

    def increment_number_served(self, amount):
        self.number_served += amount

