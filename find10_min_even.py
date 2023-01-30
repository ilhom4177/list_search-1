def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    min_even = float("inf")
    for num in data:
        if num % 2 == 0 and num < min_even:
            min_even = num
    return min_even if min_even != float("inf") else None
print(find_min_even([1, 8, 2, 8, 5]))
