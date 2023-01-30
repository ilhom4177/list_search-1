def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    l = []
    i = 0
    while i < len(data):
        if data[i] % 2 ==0:
            l.append(data[i])
        i += 1
    if l == []:
        return -1
    mx = l[0]
    i=0
    while i < len(l):
        if l[i] > mx:
            mx = l[i]
        i += 1
    
    return mx
print(find_max_even([1, 4, 3, 8, 5]))