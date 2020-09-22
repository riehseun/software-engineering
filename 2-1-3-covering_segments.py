# Uses python3
import sys
from collections import namedtuple


Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    """
    Given a set of segments on a line, find as few points on a line as
    possible so that each segment contains at least one marked point

    Args:
    segment -- array of input segments

    Returns:
    answer -- miminum number of point and all marked points
    """

    # Sort the segments by the second coordinates
    segments.sort(key=lambda x: x[1])

    clusters = []
    overlapping_coordinates = []

    while len(segments) > 0:
        cluster = []
        target_segment = segments[0]

        # Store all integers in range rather than only "from" and "to"
        item = []
        for i in range(target_segment[0], target_segment[1]+1):
            item.append(i)

        cluster.append(item)
        segments.remove(segments[0])

        new_segments = []

        for segment in segments:
            # If segments overlap
            if (segment[0] <= target_segment[1]
                and segment[1] >= target_segment[0]):
                # Both conditions satisfied

                # Store all integers in range rather than only "from"
                # and "to"
                item = []
                for i in range(segment[0], segment[1]+1):
                    item.append(i)

                cluster.append(item)

            else:
                new_segments.append(segment)

        segments = new_segments
        clusters.append(cluster)

    overlapping_values = []

    for cluster in clusters:

        overlapping_value = 0

        # Take the first item in each cluster and check all the values
        for number in cluster[0]:
            is_overlapping_value = True
            for i in range(1, len(cluster)):
                if number not in cluster[i]:
                    is_overlapping_value = False

            # Store only the biggest overlapping value
            if is_overlapping_value:
                overlapping_value = number

        overlapping_values.append(overlapping_value)

    # Construct the output
    answer = str(len(clusters))
    answer += "\n"
    for elem in overlapping_values:
        answer += str(elem)
        answer += " "

    return answer


print(optimal_points([[1,3], [2,5], [3,6]]))
print(optimal_points([[4,7], [1,3], [2,5], [5,6]]))

the_array = []
with open("test.txt", 'r') as line:

    total = line.read().split("\n")
    # print(total)

    for item in total:
        temp = []
        a = item.split(" ")
        temp.append(int(a[0]))
        temp.append(int(a[1]))

        the_array.append(temp)

print(optimal_points(the_array))



# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     print(optimal_points(segments))