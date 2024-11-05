import math

# Function to calculate the distance between two drones
def calculate_distance(drone1, drone2):
    return math.sqrt((drone1.x - drone2.x)^2 + (drone1.y - drone2.y)^2)

# Function to find the closest pair of drones in a given set
def find_closest_pair(drones):
    n = len(drones)

    # Base case: if there are fewer than 3 drones, brute force check
    if n <= 3:
        return min(calculate_distance(drones[i], drones[j]) for i in range(n) for j in range(i+1, n))

    # Sort drones based on x-coordinates
    drones.sort(key=lambda drone: drone.x)

    # Recursively find the closest pair in the left and right halves
    mid = n // 2
    left_half = drones[:mid]
    right_half = drones[mid:]

    min_left = find_closest_pair(left_half)
    min_right = find_closest_pair(right_half)

    # Find the minimum distance among the left and right halves
    min_distance = min(min_left, min_right)

    # Check for drones with x-coordinates close to the middle
    strip = [drone for drone in drones if abs(drone.x - drones[mid].x) < min_distance]

    # Sort the strip based on y-coordinates
    strip.sort(key=lambda drone: drone.y)

    # Compare the distances within the strip
    min_strip = min(calculate_distance(strip[i], strip[j]) for i in range(len(strip)) for j in range(i+1, len(strip)))

    # Return the minimum distance among the three cases
    return min(min_distance, min_strip)

# Pseudo code for the algorithm
def closest_pair_of_drones(drones):
    drones.sort(key=lambda drone: drone.x)
    return find_closest_pair(drones)
