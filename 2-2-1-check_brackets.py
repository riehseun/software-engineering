# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


def is_balanced(string):
    """

    """

    stack = []

    for char in string:

        if char == "[" or char == "(" or char == "{":
            stack.append(char)

        else:
            if not stack:
                return "Success"

            top = stack.pop()
            if ((top == "[" and char != "]")
                or (top == "(" and char != ")")
                or (top == "{" and char != "}")):
                # One of three conditions satisfy

                print(stack)
                return string.index(char) + 1

    print(stack)
    if not stack:
        return "Success"
    else:
        return string.index(char) + 1


print(is_balanced("[]"))
print(is_balanced("{}[]"))
print(is_balanced("[()]"))
print(is_balanced("(())"))
print(is_balanced("{[]}()"))
print(is_balanced("{"))
print(is_balanced("{[}"))
print(is_balanced("foo(bar);"))
print(is_balanced("foo(bar[i);"))


# if __name__ == "__main__":
#     main()
