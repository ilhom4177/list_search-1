def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    evens = [num for num in data if num % 2 == 1]
    return min(evens) if evens else None

print(find_min_odd([1,23,42,21,11,33]))