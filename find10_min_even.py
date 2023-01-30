def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    evens = [num for num in data if num % 2 == 0]
    return min(evens) if evens else -1
print(find_min_even([1, 8, 2, 8, 5]))
