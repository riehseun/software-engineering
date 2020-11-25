import sys
import threading
import time

from collections import deque


def compute(n, parents):
    """
    Inverts array representation of tree into dictionary representation
    of tree. Then, computes the height of the tree

    Args:
    n -- number of nodes in the tree
    parents -- array representation of tree

    Returns:
    The height of tree
    """

    # start_time = time.time()
    tree = {}
    root = -1

    for i in range(len(parents)):
        tree[i] = []

    for i in range(len(parents)):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    # print("--- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    # Compute height using BFS
    data = bfs(tree, root)
    nodes = data[0]
    last_item = data[1]
    return compute_height_from_bfs(nodes, last_item, [0]) + 1
    # print("--- %s seconds ---" % (time.time() - start_time))

    # Compute height by constructing subtrees
    return compute_height(tree, root)


def compute_height(tree, root):
    """
    Computes the height of the tree

    Args:
    tree -- dictionary representation of tree
    root -- root node of tree

    Returns:
    The height of tree
    """

    # If empty tree
    if len(tree) == 0:
        return 1

    # Root has no children
    if len(tree[root]) == 0:
        return 1

    child_heights = []

    # Traverse all children of the root node
    for node in tree[root]:
        child_tree = find_subtree(tree, node, {})
        child_heights.append(compute_height(child_tree, node))

    # print(child_heights)
    return 1 + max(child_heights)


def find_subtree(tree, root, subtree):
    """
    Computes the subtree (with given root) of the tree

    Args:
    tree -- dictionary representation of tree
    subtree - dictionary representation of subtree (to be filled)
    root -- root node of subtree

    Returns:
    Dictionary representation of subtree
    """

    for key, val in tree.items():
        if key == root and key not in subtree:
            subtree[key] = val
            for node in val:
                find_subtree(tree, node, subtree)

    return subtree


def bfs(tree, root):
    """
    Performs breath first search on tree

    Args:
    tree -- dictionary representation of tree
    root -- root node of tree

    Returns:
    Result of the BFS and the last node of the tree
    """

    if len(tree) == 0:
        return

    # This will be the ouput of the breath-first search
    nodes = {}
    last_item = -1

    queue = deque()
    v = {}
    v[root] = tree[root]
    queue.append(v)
    while len(queue) > 0:
        node = queue.popleft()

        # Stores the relationship such that child is the key and parent
        # is the value. This is for easy traversal to calculate the
        # height of the tree. The root of the tree will be excluded
        # since it does not have a parent
        for item in node[next(iter(node))]:
            nodes[item] = next(iter(node))
        # nodes[next(iter(node))] = node[next(iter(node))]

        for child in node[next(iter(node))]:
            v = {}
            v[child] = tree[child]
            queue.append(v)
            last_item = child

    return (nodes, last_item)


def compute_height_from_bfs(nodes, child, height):
    """
    Compute height of the tree from the result of BFS

    Args:
    nodes -- Result of the BFS
    child -- node to start searching to compute the height
    height -- keeping track of height of the tree while searching

    Returns:
    The height of the tree
    """

    # print(nodes)
    # print(child)
    # print(root)

    # if child == root:
    #     return height[0]

    # for key, val in nodes.items():
    #     for item in val:
    #         if child == item:
    #             height[0] += 1
    #             return compute_height_from_bfs(nodes, root, key, height)

    if child not in nodes:
        return height[0]

    for key, val in nodes.items():
        if key == child:
            height[0] += 1
            return compute_height_from_bfs(nodes, val, height)


# print(compute(5, [4,-1,4,1,1]))
# print(compute(5, [-1,0,4,0,3]))
# print(compute(10, [9,7,5,5,2,9,9,9,2,-1]))
# def conv(arr):
#     temp = arr.split(" ")
#     ret = []
#     for item in temp:
#         print(item)
#         ret.append(int(item))
#     return ret


def main():
    # print(compute(5, [4,-1,4,1,1]))
    # print(compute(5, [-1,0,4,0,3]))
    # print(compute(10, [9,7,5,5,2,9,9,9,2,-1]))
    # print(compute(10000, conv("21758 39525 8199 17018 29420 52135 83354 12001 52975 54159 95056 62209 31036 48368 6569 21744 6110 42543 9761 1392 46723 20677 11511 71551 52800 37451 84698 2341 72950 45108 80559 22363 7066 62482 95863 60566 26234 44450 3018 84958 17537 3415 43540 62233 83530 20482 72959 81160 55035 60979 10872 92611 68962 23782 63538 1850 74825 28828 8063 17327 30354 81817 23641 26303 11766 61841 53373 65264 39907 7706 50293 72360 47497 70831 17552 35817 13252 30949 80977 94561 25 82718 27867 58266 9590 41004 54174 62324 93635 35177 75206 84563 70980 251 17559 8784 94186 13520 54799 40299 5113 57261 69773 99270 21439 57813 45632 78641 41589 23150 94034 93766 65503 60181 12710 23521 71227 87432 6642 72537 82170 72615 28181 39572 51540 58520 29260 28738 9388 72015 5544 94322 13974 77819 23828 51746 11627 28021 50768 56755 40330 33936 44883 61783 65735 2590 35623 28374 53571 37673 78873 41774 30278 42278 71410 95258 70098 58050 61763 6258 6040 27035 3602 23671 97560 2253 42560 57518 48662 26108 9341 46468 29198 23396 57788 14163 13994 58924 50061 31546 41238 48184 42161 19483 27359 82168 94254 35147 33496 72777 58272 61810 62652 4977 81883 2924 93770 735 86328 799 9442 27778 13805 16463 55967 50771 50040 82211 53706 56403 84252 43280 66934 37110 48648 32860 99105 41784 1594 30798 48917 77597 48807 86091 24143 76575 80729 34029 85616 43680 91368 71293 31066 6348 52956 67667 55771 27460 51307 90238 57578 86694 56754 68711 32615 1277 36744 79020 29612 77404 65366 91806 7989 72751 66759 73875 93114 13748 34770 73579 93208 35180 41639 58409 80475 92269 10440 55563 50811 86627 80115 14240 17955 33908 70167 72341 34884 2974 90333 57240 51816 39304 56908 54238 37748 40521 9897 15268 98622 92624 83517 99015 98175 43219 60343 49498 84073 93109 33119 39749 80858 31235 36019 71269 10783 33823 86852 38638 53084 79218 42671 17611 55023 78819 4675 48857 98117 77100 76331 14032 1173 98314 40159 45687 6094 60942 61725 75246 34377 75055 84930 32377 99898 48299 247 60996 67660 42740 65895 46840 55851 59660 42765 47841 48976 55552 18750 51678 6157 91449 2293 12914 99842 87093 92912 44088 81000 44338 64833 70114 80046 28117 77323 47062 9706 55315 95804 37747 51295 27545 78458 83292 64086 96963 68401 10840 84798 68023 89094 23674 17796 87166 16795 64468 61500 3514 21090 21717 55528 7798 84921 33063 85373 11195 81744 73712 60069 45551 4662 12649 94497 71217 3533 72564 87592 104 ... 3278 24050 50703 77473 83121 88602 15597 89931 2762 33568 24391 18564 49860 71053 58054 9285 88439 94289 46062 94894 45064 10491 73072 99496 56878 86795 37015 57798 65087 26346 79316 54844 35488 56867 77504 5020 82155 546 32332 81088 29583 82441 33318 91397 9825 12567 84940 98577 64202 2641 95512 88181 25839 20518 80701 56745 91160 35650 35348 90220 83926 90455 61025 89811 73327 65143 4103 39996 78986 57304 67067 82259 89416 90211 16221 71759 70602 36357 84292 42312 82865 10280 34218 45627 48825 70561 56202 34541 33477 21357 19253 60381 64265 66501 87242 87375 16345 82271 71983 53535 45755 1008 24293 30325 86084 49252 41049 29244 64102 48332 10192 20528 16597 8440 35521 2420 97863 16461 43042 25692 10395 98871 49547 88660 21816 52298 58393 35302 21352 70734 36486 16372 27500 32233 45152 64650 16868 26408 99068 23709 34325 47376 13257 87336 61682 56875 81686 8749 42112 64091 12329 85740 96662 95140 98823 52823 94068 4525 40059 72491 89581 33611 51586 84240 73555 83277 4086 57876 52970 8339 6380 36806 68291 97111 49567 1428 30956 31755 24278 19110 91543 56802 82014 14798 68286 89309 83260 51557 50793 51279 77484 24455 97723 10148 15589 49608 68859 65095 63012 46722 49426 31643 13978 46740 12056 94462 78242 72277 91587 1650 61362 75305 88373 37821 86637 72487 82473 35497 36303 42156 78344 77617 67922 13779 33670 54803 47961 72150 71857 61702 10809 17236 66741 33041 27803 61067 46122 23624 83702 54718 15214 63063 34452 43786 30396 72927 26211 60863 1567 18705 56983 63401 35207 94508 20862 81309 24036 50342 74864 42812 10850 85018 60855 47927 20322 33655 91760 14447 19381 13251 34142 20888 89941 28275 36394 15932 72864 38222 25732 14030 75674 9648 24847 93064 33740 45549 60256 11067 97010 91933 82330 36884 80208 50119 5308 5541 15807 78152 82701 64089 21588 18587 56660 69598 92377 26684 95941 39336 83423 75065 98207 59618 84088 84807 87634 86143 44098 25786 15299 57177 87911 9036 99132 37208 79893 92367 91346 26536 96257 88640 37855 51466 36540 5652 39763 48988 96680 22624 74120 69107 16150 23789 38013 36345 63132 75856 13149 76721 99287 7212 34265 94748 71443 3474 47557 39310 29689 87800 41491 68412 95183 89883 83077 37166 98223 47205 91547 9903 68737 84049 84053 94192 7666 11717 30942 6522 90878 92578 76950 82743 41056 20285 14289 75147 83108 55434 94891 56518 16892 47703 74468 33181 71181 50911 93709 30361 22381")))
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()