def city_country(city, country, population=''):
    """Generate a neatly formatted single string with city and country"""
    if population:
        full_name = city + ',' + ' ' + country + ' - Population ' + str(population)
    else:
        full_name = city + ',' + ' ' + country
    return full_name.title()
