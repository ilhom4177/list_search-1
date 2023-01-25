def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i=0 
    max1 = 0
    while i < len(data):
        if max1 < data[i] and data[i] % 2 == 1:
            max1 = data[i]
        i += 1
    return max1 
