def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    even_numbers = [x for x in data if x % 2 == 0]
    return max(even_numbers)
