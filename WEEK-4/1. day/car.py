def ride(car,km):
    car['km'] += km

def init_car(color, type,km):
    car ={'color':'','type':'', 'km': 0}
    car['color'] = color
    car['type'] = type
    car['km'] = km
    return car

lada = init_car('red', 'Lada 1200', 40000)
tesla = init_car('pink', 'Tesla S', 1200)



ride(tesla, 220)
print(tesla)
