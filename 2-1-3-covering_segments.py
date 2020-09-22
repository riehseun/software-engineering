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

    overlapping_values = set()
    for cluster in clusters:
        # Take the first item in each cluster and check all the values
        for number in cluster[0]:
            for i in range(1, len(cluster)):
                is_overlapping_value = True
                if number not in cluster[i]:
                    is_overlapping_value = False

            if is_overlapping_value:
                overlapping_values.add(number)

    # Construct the output
    answer = str(len(clusters))
    answer += "\n"
    for elem in overlapping_values:
        answer += str(elem)

    return answer


print(optimal_points([[1,3], [2,5], [3,6]]))
print(optimal_points([[4,7], [1,3], [2,5], [5,6]]))


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     points = optimal_points(segments)
#     # print(len(points))
#     print(*points)