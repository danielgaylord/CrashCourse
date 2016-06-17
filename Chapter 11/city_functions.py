def display_city(city, country, population=0):
    display = city.title() + ", " + country.title()
    if population != 0:
        display += " - population " + str(population)
    return display
