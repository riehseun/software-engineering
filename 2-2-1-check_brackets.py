def is_balanced(string):
    """
    Check if all the opening brackets in the string are properly closed

    Args:
    string -- input string containing brackets

    Returns:
    Success if all opening brackets are properly closed. Otherwise,
    outputs the index of the opening bracket that is not closed
    """

    # opening_brackets = {}
    opening_brackets = []
    stack = []

    for i in range(len(string)):

        # If opening bracket
        if string[i] in ["[", "(", "{"]:
            stack.append((i+1, string[i]))

        else:
            # If closing bracket
            if string[i] in ["]", ")", "}"]:
                if not stack:
                    return i + 1

                top = stack.pop()

                if ((top[1] == "[" and string[i] != "]")
                    or (top[1] == "(" and string[i] != ")")
                    or (top[1] == "{" and string[i] != "}")):
                    # One of three conditions satisfy

                    return i + 1

    if not stack:
        return "Success"

    else:
        remaining_opening_bracket = stack.pop()
        return remaining_opening_bracket[0]


print(is_balanced("[]"))
print(is_balanced("{}[]"))
print(is_balanced("[()]"))
print(is_balanced("(())"))
print(is_balanced("{[]}()"))
print(is_balanced("{"))
print(is_balanced("{[}"))
print(is_balanced("foo(bar);"))
print(is_balanced("foo(bar[i);"))
