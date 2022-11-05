def make_car(manufacturer, model, **others):
    """function that makes a car"""
    car_description = {'manufacturer': manufacturer.title(),
                       'model': model.title(),
                       }
    for key, value in others.items():
        car_description[key] = value

    return car_description


car = make_car('Volkswage', 'Passat', color='red', navigator=True)
print(car)

