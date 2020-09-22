#Uses python3
import sys


def largest_number(a):
    """

    """

    array = new_quick_sort(a)

    # print(array)

    largest_number = ""

    for number in array:
        largest_number += str(number)

    return largest_number


def new_quick_sort(a):
    """

    """

    if len(a) <= 1:
        return a

    pivot = a[0]
    partition1 = []
    partition2 = []

    for i in range(1,len(a)):
        if len(str(a[i])) == len(str(pivot)):
            if a[i] > pivot:
                partition1.append(a[i])
            elif a[i] <= pivot:
                partition2.append(a[i])

        else:
            # Compare the first digits
            u = int(str(a[i])[0])
            v = int(str(pivot)[0])

            if u > v:
                partition1.append(a[i])
            elif u < v:
                partition2.append(a[i])
            else:
                # In this case, one must be a 2 digits number and the
                # other must be a 3 digits number
                if len(str(a[i])) >= 2 and len(str(pivot)) >= 2:
                    # Compare the first two digits
                    uu = int(str(a[i])[0] + str(a[i])[1])
                    vv = int(str(pivot)[0] + str(pivot)[1])

                    if uu > vv:
                        partition1.append(a[i])
                    elif uu < vv:
                        partition2.append(a[i])
                    else:
                        if len(str(a[i])) > len(str(pivot)):
                            if int(str(a[i])[2]) > int(str(pivot)[1]):
                                partition1.append(a[i])
                            else:
                                partition2.append(a[i])
                        else:
                            if int(str(a[i])[1]) < int(str(pivot)[2]):
                                partition2.append(a[i])
                            else:
                                partition1.append(a[i])
                else:
                    if len(str(a[i])) > len(str(pivot)):
                        if int(str(a[i])[1]) > int(str(pivot)[0]):
                            partition1.append(a[i])
                        else:
                            partition2.append(a[i])
                    else:
                        if int(str(a[i])[0]) < int(str(pivot)[1]):
                            partition2.append(a[i])
                        else:
                            partition1.append(a[i])


    return new_quick_sort(partition1) + [pivot] + new_quick_sort(partition2)


# print(largest_number([21,2]))
# print(largest_number([9,4,6,1,9]))
# print(largest_number([23,39,92]))


print(largest_number([232,23]))
print(largest_number([606,60]))

# 23232
# 60660

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))