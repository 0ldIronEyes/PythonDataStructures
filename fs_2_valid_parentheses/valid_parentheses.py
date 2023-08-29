def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    leftparen = 0
    rightparen = 0
    for char in parens:
        if char == "(":
            leftparen += 1
        if char == ")":
            rightparen += 1

    if leftparen == rightparen:
        return True
    else:
        return False