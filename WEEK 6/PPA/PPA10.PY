def group_by_city(scores_dataset):
    cities = dict()
    for student in scores_dataset:
        city = student['City']
        name = student['Name']
        if city not in cities:
            cities[city] = [ ]
        cities[city].append(name)
    return cities
def busy_cities(scores_dataset):
 cities = group_by_city(scores_dataset)
 busy = [ ]
 maxpop = 0
 for city in cities:
    if len(cities[city]) > maxpop:
        maxpop = len(cities[city])
        busy = [city]
    elif len(cities[city]) == maxpop:
        busy.append(city)
 return busy
    
