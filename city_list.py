# List of cities supported to be replaced by SQL statement
cities_list = ['Lake District National Park', 'Corfe Castle', 'The Cotswolds', 'Cambridge', 'Bristol',
                   'Oxford', 'Norwich', 'Stonehenge', 'Watergate Bay', 'Birmingham']
# Function to find all occurrences of supported cities in string
def extract_cities(string):
    detected_cities = []
    total_num = len(cities_list)
    for i in range(total_num):
        city = cities_list[i]
        if city.lower() in string.lower():
            detected_cities.append(city)
    return detected_cities
