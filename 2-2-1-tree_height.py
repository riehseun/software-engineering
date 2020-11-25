import sys
import threading


def compute(n, parents):
    """

    """

    tree = {}
    root = -1

    for i in range(len(parents)):
        tree[i] = []

    for i in range(len(parents)):
        if parents[i] == -1:
            # print("root:"+str(i))
            root = i
        else:
            tree[parents[i]].append(i)

    return compute_height(tree, root)


def compute_height(tree, root):
    """

    """

    print("tree:"+str(tree))
    print("root:"+str(root))
    # print("len:"+str(len(tree)))


    if len(tree) == 0:
        return 1

    # Root has no children
    if len(tree[root]) == 0:
        return 1

    # Root has one child
    if len(tree[root]) == 1:
        child_root = tree[root][0]
        child_tree = find_subtree(tree, child_root, {})
        return 1 + compute_height(child_tree, child_root)

    # Root has two children
    elif len(tree[root]) == 2:
        left_root = tree[root][0]
        right_root = tree[root][1]
        left_tree = find_subtree(tree, left_root, {})
        right_tree = find_subtree(tree, right_root, {})
        print(left_tree)
        print(right_tree)
        return 1 + max(compute_height(left_tree, left_root), compute_height(right_tree, right_root))


def find_subtree(tree, root, subtree):
    """

    """

    for key, val in tree.items():
        if key == root and key not in subtree:
            subtree[key] = val
            for node in val:
                # print(subtree)
                find_subtree(tree, root, subtree)

    return subtree



# 0 1 2 3 4 => 3 | 4 0 2
# ({3:[]},3) ({4: [0, 2]}, 4)






# Height(tree)
# if tree = nil
#     return 0
# return 1 + Max(Height(tree.left), Height(tree.right))



def main():
    print(compute(5, [4,-1,4,1,1]))
    print(compute(5, [-1,0,4,0,3]))

    # n = int(input())
    # parents = list(map(int, input().split()))
    # print(compute(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
