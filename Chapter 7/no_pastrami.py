sandwich_orders = ['tuna melt', 'pastrami', 'hoagie', 'pastrami', 'gyro', 'pastrami']
hold = 'pastrami'

while hold in sandwich_orders:
    sandwich_orders.remove(hold)

print("\nThe new orders, holding " + hold)
for sandwich in sandwich_orders:
    print("\t" + sandwich)
