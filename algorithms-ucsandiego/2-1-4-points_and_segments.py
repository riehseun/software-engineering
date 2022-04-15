# Uses python3
import sys


def count_segments(starts, ends, points):
    """
    For each point, find the number of segments that contain this point

    Args:
    starts -- list of starting points of segments
    ends -- list of ending points of segments
    points -- points to check

    Returns:
    the number of segments that contain each point given in the input
    list "points"
    """

    count = 0
    data = []
    answer = {}
    string = ""

    for elem in starts:
        data.append([elem, "L"])

    for elem in ends:
        data.append([elem, "R"])

    for elem in points:
        data.append([elem, "P"])

    # sort by the first item, then by type (so that left coordinate
    # comes before the point)
    sorted_data = sorted(data, key=lambda x: (x[0],x[1]), reverse=False)

    for item in sorted_data:
        if item[1] == "L":
            count += 1
        elif item[1] == "R":
            count -= 1
        elif item[1] == "P":
            if count < 0:
                answer[item[0]] = 0
            else:
                answer[item[0]] = count

    for point in points:
        string += str(answer[point])
        string += " "

    return string[:-1]


print(count_segments([0,7], [5,10], [1,6,11]))
print(count_segments([-10], [10], [-100,100,0]))
print(count_segments([0,-3,7], [5,2,10], [1,6]))