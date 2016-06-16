def make_car(make, model, **info):
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in info.items():
        car[key] = value
    return car

print(make_car('nissan', 'altima', color='silver', year='2012', other='other'))