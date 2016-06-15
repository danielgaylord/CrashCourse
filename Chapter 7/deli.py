sandwich_orders = ['tuna melt', 'hoagie', 'gyro']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I just ate your " + sandwich)
    finished_sandwiches.append(sandwich)

print("\nI just ate the following sandwiches: ")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)
