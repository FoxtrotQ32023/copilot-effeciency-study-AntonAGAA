# I need to find the best hub with a given set of inputs that represent coordinates of airports

# these are the inputs:

# 1 <= n <= 1000
# n lines follow, each giving the latitude (between -180 and +180 degrees) and longitude (between -90 and +90 degrees) of an airport.
# The input floating point numbers will not have more than two digits after the decimal point.
# Input is terminated by end of file.

# I need to find the best hub with a given set of inputs that represent coordinates of airports

# these are the inputs:

# based on the input, I need to find the best hub

# For each set of input print the latitude and longitude of the airport that best serves as a hub in a single line.  
# If there is more than one airport that best serves as a hub print the one that appears last in the input of the corresponding input set.  
# Your output should always contain two digits after the decimal point.


content = """
    3
    3.2 -15.0
    20.1 -175
    -30.2 10
    3
    52.31 4.76
    51.96 4.44
    51.45 5.37
    """

def find_airport_hubs(content):
    """
    Function to determine the best hubs from the given content string.
    """
    calculate_distance = lambda x1, y1, x2, y2: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    lines = content.strip().split('\n')
    idx = 0
    hubs = []

    while idx < len(lines):
        n = int(lines[idx].strip())
        idx += 1
        
        airports = []
        for i in range(n):
            x, y = map(float, lines[idx].split())
            airports.append((x, y))
            idx += 1
        
        best_hub = None
        best_hub_distance = float('inf')  # Initialize with a large value
        for airport in airports:
            max_distance_for_airport = max(calculate_distance(airport[0], airport[1], other_airport[0], other_airport[1]) for other_airport in airports)
            if max_distance_for_airport < best_hub_distance:
                best_hub = airport
                best_hub_distance = max_distance_for_airport
                
        hubs.append((round(best_hub[0], 2), round(best_hub[1], 2)))
    print(hubs)
    return hubs


find_airport_hubs(content)