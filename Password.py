import math

# Function to calculate distance between two cities
def distance_between_cities(city1, city2, unit):
    # Coordinates for city1 and city2
    city1_lat = city1[0]
    city1_long = city1[1]
    city2_lat = city2[0]
    city2_long = city2[1]

    # Convert latitude and longitude to radians
    city1_lat_rad = math.radians(city1_lat)
    city1_long_rad = math.radians(city1_long)
    city2_lat_rad = math.radians(city2_lat)
    city2_long_rad = math.radians(city2_long)

    # Calculate distance
    distance = math.acos(math.sin(city1_lat_rad) * math.sin(city2_lat_rad) + 
                         math.cos(city1_lat_rad) * math.cos(city2_lat_rad) * 
                         math.cos(city1_long_rad - city2_long_rad))

    # Convert distance to specified unit
    if unit == "km":
        distance = distance * 6371
    elif unit == "mi":
        distance = distance * 3959
    elif unit == "m":
        distance = distance * 6371000
    elif unit == "ft":
        distance = distance * 20898800
    else:
        return "Invalid unit"
    
    # Round distance to 2 significant figures
    distance = '{:.2g}'.format(distance)
    return distance

# Example usage
city1 = (37.788022, -122.399797) # San Francisco
city2 = (40.730610, -73.935242) # New York City
unit = "km"
print(distance_between_cities(city1, city2, unit))
