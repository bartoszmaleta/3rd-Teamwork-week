def maximum(elements):
    """
    Returns a maximum number from a list.

    >>> maximum([1, 2, 3])
    3
    """

    best = 0
    for element in elements:
        if element > best:
            best = element
    return best