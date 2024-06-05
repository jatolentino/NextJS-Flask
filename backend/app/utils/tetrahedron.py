import numpy as np
from itertools import combinations

# Tetrahedron volume calculation
def volume_of_tetrahedron(p1, p2, p3, p4):
    AB = p2[:3] - p1[:3]
    AC = p3[:3] - p1[:3]
    AD = p4[:3] - p1[:3]

    # Cross product of AB and AC
    cross_product = np.cross(AB, AC)

    # Dot product of AD with the cross product of AB and AC
    scalar_triple_product = np.dot(cross_product, AD)

    # The volume of the tetrahedron
    volume = abs(scalar_triple_product) / 6.0
    return volume

# Finding the smallest Tetrahedron
def find_smallest_tetrahedron(file_path):
    # Loading the input file data: file_path
    points = np.loadtxt(file_path, delimiter=',')
    valid_tetrahedrons = []

    # Finding all combinations of 4 points
    for comb in combinations(range(len(points)), 4):
        subset = points[list(comb)]
        if subset[:, 3].sum() == 100:
            valid_tetrahedrons.append(comb)

    # Calculating the volume of each valid tetrahedron and finding the one with the smallest volume
    min_volume = float('inf')
    best_tetrahedron = None

    # Return and print the indices in ascending order
    for comb in valid_tetrahedrons:
        p1, p2, p3, p4 = points[list(comb)]
        volume = volume_of_tetrahedron(p1, p2, p3, p4)
        if volume < min_volume:
            min_volume = volume
            best_tetrahedron = comb

    # Sorting according to indexes in ascending order. This is the solution :D
    best_tetra_list = sorted(best_tetrahedron)

    # Retrieving the points from the indexes of the best_tetra_list
    best_tetrahedron_points = []
    for best in best_tetra_list:
        best_tetrahedron_points.append(tuple(points[best][:3]))

    # Storing the tetrahedron points onto a JSON data-structure-like for posterior API requests 
    data = {
        "indexes_solution": best_tetra_list,
        "first_point": [*best_tetrahedron_points[0]],
        "second_point": [*best_tetrahedron_points[1]],
        "third_point": [*best_tetrahedron_points[2]],
        "fourth_point": [*best_tetrahedron_points[3]]
    }
    return best_tetra_list, data
