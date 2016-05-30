pizzas = ['hawaiian', 'meat lovers', 'the works']
for pizza in pizzas:
    print("I genuinely like " + pizza + " pizza")

print("\nPizza is good.\nPizza is great.\nIf I eat too much,\nI gain lots of weight!")

friend_pizzas = pizzas[:]

pizzas.append('vegetarian')
friend_pizzas.append('stuffed-crust')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
