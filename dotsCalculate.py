import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage:
# Coordinates of two points on the football field
point1 = (10, 20)  # Replace with actual coordinates
point2 = (30, 40)  # Replace with actual coordinates

# Calculate distance
distance_between_points = calculate_distance(point1[0], point1[1], point2[0], point2[1])

# Print the result
print(f"The distance between the two points is: {distance_between_points} units (e.g., yards)")
