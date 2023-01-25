def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    i = 0
    n = data[0]
    while i < len(data):
        if n > data[i]:
            n = data[i]
        i += 1
    return n