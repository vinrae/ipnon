import numpy as np

def calculate_centroid(points):
    points_array = np.array(points)
    centroid = np.mean(points_array, axis=0)
    return centroid

# Example usage:
points = [(0, 0), (4, 0), (4, 3), (0, 3)]
centroid = calculate_centroid(points)
print(f"The centroid is at {centroid}")
