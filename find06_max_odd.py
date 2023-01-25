def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    odd_numbers = filter(lambda x: x % 2 != 0, data)
    return max(odd_numbers, default=None)
print(find_max_odd([1, 8, 3, 8, 5]))