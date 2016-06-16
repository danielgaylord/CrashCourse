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


burger_king = Restaurant("bUrger King", 'Noble')
print(burger_king.restaurant_name)
print(burger_king.cuisine_type)
burger_king.describe_restaurant()
burger_king.open_restaurant()
print(str(burger_king.number_served) + " served so far")
burger_king.increment_number_served(100)
print(str(burger_king.number_served) + " served so far")

gs = Restaurant("golden sun", 'chinese')
sw = Restaurant("sapphire wednesday", "american")

gs.describe_restaurant()
sw.describe_restaurant()
