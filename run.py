import math
import random
import collections


def DFS_ordering(graph, node, explored_ordering):
    explored_ordering.append(node)
    for vertex in get_next(graph, node):
        if vertex not in explored_ordering:
            DFS_ordering(graph, vertex, explored_ordering)
    ordering.append(node)


def DFS_loop_ordering(graph, max_integer):
    i = max_integer
    while i > 0:
        if i not in explored_ordering:
            DFS_ordering(graph, i, explored_ordering)
        i = i - 1


def DFS_loop_computing(graph, max_integer):
    i = max_integer
    s[0] = 0
    while i > 0:
        if i not in explored_computing:
            s[0] = i
            DFS_computing(graph, i, explored_computing)
        i = i - 1


def DFS_computing(graph, node, explored_computing):
    explored_computing.append(node)
    leader.append(s[0])
    for vertex in get_next(graph, node):
        if vertex not in explored_computing:
            DFS_computing(graph, vertex, explored_computing)


def get_next(graph, node):
    vertices = []
    for arc in graph:
        if arc[0] == node:
            vertices.append(arc[1])
    return vertices


def compute_max(graph):
    temp_list = []
    for edge in graph:
        temp_list.append(max(edge[0], edge[1]))
    return max(temp_list)


def open_graph(file_path):
    """
    Imports a file and stored data into a list of lists

    Args:
    file_path -- location of file

    Returns
    graph -- adjacency representation of graph (a list of lists)
    """

    graph = []

    with open(file_path, 'r') as line:
        array = line.read().split("\n")
        for subarray in array:
            graph.append(subarray.split(" "))

    for arc in graph:
        arc[0] = int(arc[0])
        arc[1] = int(arc[1])

    return graph


# graph = open_graph("data/strongly-connected-component-test1.txt")
# graph = open_graph("data/strongly-connected-component-test2.txt")
# graph = open_graph("data/strongly-connected-component-test3.txt")
# graph = open_graph("data/strongly-connected-component-test4.txt")
# graph = open_graph("data/strongly-connected-component-test5.txt")
graph = open_graph("data/strongly-connected-component.txt")


# Compute the magical ordering
ordering = []
explored_ordering = []
DFS_loop_ordering(graph, compute_max(graph))
# print(ordering)


# Reverse direction of graph
for edge in graph:
    tmp = edge[0]
    edge[0] = edge[1]
    edge[1] = tmp
# print(graph)


# Change nodes based on magical ordering
for i in range(0, len(graph)):
    graph[i][0] = ordering.index(graph[i][0]) + 1
    graph[i][1] = ordering.index(graph[i][1]) + 1
# print(graph)


# Compute the strongly connected components
leader = []
explored_computing = []
s = []
s.append(-1) # leaders in second path
DFS_loop_computing(graph, compute_max(graph))
# print(leader)


# Show the result
counter = collections.Counter(leader)
print(counter.values())
print(counter.most_common(5))