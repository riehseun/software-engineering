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

        cluster.append(target_segment)
        segments.remove(segments[0])

        new_segments = []

        for segment in segments:
            # If segments overlap
            if (segment[0] <= target_segment[1]
                and segment[1] >= target_segment[0]):
                # Both conditions satisfied
                cluster.append(segment)
            else:
                new_segments.append(segment)

        segments = new_segments
        clusters.append(cluster)

    overlapping_values = []

    for cluster in clusters:
        # Smallest value of the second coordinates in the sorted list
        # should be the largest common integer
        cluster.sort(key=lambda x: x[1])
        overlapping_values.append(cluster[0][1])

    # Construct the output
    answer = str(len(clusters))
    answer += "\n"
    for elem in overlapping_values:
        answer += str(elem)
        answer += " "

    return answer


print(optimal_points([[1,3], [2,5], [3,6]]))
print(optimal_points([[4,7], [1,3], [2,5], [5,6]]))