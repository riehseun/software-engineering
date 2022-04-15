#Uses python3
import sys
import math


def minimum_distance(xs, ys):
    """
    Find the minimum euclidean distance from all coordinates

    Args:
    xs -- x coordinates
    ys -- y coordinates

    Returns:
    minimum -- the minimum euclidean distance
    """

    coordinates = []

    for i in range(len(xs)):
        coordinates.append([xs[i],ys[i]])

    return minimum_distance_subroutine(coordinates)


def minimum_distance_subroutine(coordinates):
    """
    Find the minimum euclidean distance from all coordinates

    Args:
    coodinates -- all (x,y) coordinates

    Returns:
    minimum -- the minimum euclidean distance
    """

    if len(coordinates) <= 3:
        return brute_force_search(coordinates)

    # Sort by x-coordinate
    sorted_coordinates = sorted(coordinates, key=lambda x: x[0])
    mid = math.floor(len(sorted_coordinates)/2)
    first_half = sorted_coordinates[:mid]
    second_half = sorted_coordinates[mid:len(coordinates)]

    min1 = minimum_distance_subroutine(first_half)
    min2 = minimum_distance_subroutine(second_half)

    minimum = min(min1, min2)

    x_from_first_half = sorted_coordinates[mid-1][0]
    x_from_second_half = sorted_coordinates[mid][0]

    coordinates_to_check = []

    for coord in first_half:
        if abs(coord[0] - x_from_second_half) <= minimum:
            coordinates_to_check.append(coord)

    for coord in second_half:
        if abs(coord[0] - x_from_first_half) <= minimum:
            coordinates_to_check.append(coord)

    # Sort by y-coordinate
    sorted_coordinates_to_check = sorted(
        coordinates_to_check, key=lambda x: x[1])

    min3 = brute_force_search(sorted_coordinates_to_check)

    return min(minimum, min3)


def brute_force_search(coordinates):
    """
    Find the minimum euclidean distance from all coordinates

    Args:
    coodinates -- all (x,y) coordinates

    Returns:
    minimum -- the minimum euclidean distance
    """

    minimum = 100000000000000000000

    j = 0
    while j < len(coordinates):
        k = j + 1

        # Only need to check 7 subsequet points at most
        while k < min(len(coordinates), j+8):
            dist = get_euclidean_distance(
                coordinates[j], coordinates[k])

            if dist < minimum:
                minimum = dist

            k += 1

        j += 1

    return minimum


def get_euclidean_distance(a, b):
    """
    Find euclidean distance of two coordinates
    """

    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))


print(minimum_distance([0,3], [0,4]))
print(minimum_distance([7,1,4,7], [7,100,8,7]))
print(minimum_distance([4,-2,-3,-1,2,-4,1,-1,3,-4,-2], [4,-2,-4,3,3,0,1,-1,-1,2,4]))