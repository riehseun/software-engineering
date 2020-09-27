# Uses python3
import sys


def count_segments(starts, ends, points):
    """

    """

    count = 0
    data = {}
    answer = {}
    string = ""

    for elem in starts:
        data[elem] = "L"

    for elem in ends:
        data[elem] = "R"

    for elem in points:
        data[elem] = "P"

    # sort by key, then by value (so that left coordinate comes before the point)
    sorted_data = sorted(data.items(), key=lambda x: (x[0],x[1]), reverse=False)

    for key, value in sorted_data:
        if value == "L":
            count += 1
        elif value == "R":
            count -= 1
        else:
            if count < 0:
                answer[key] = 0
            else:
                answer[key] = count
            count = 0

    for point in points:
        string += str(answer[point])
        string += " "

    return string[:-1]


# print(count_segments([0,7], [5,10], [1,6,11]))
# print(count_segments([-10], [10], [-100,100,0]))
# print(count_segments([0,-3,7], [5,2,10], [1,6]))




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
