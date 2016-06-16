from restaurant import Restaurant

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
