def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    l = []
    i = 0
    while i < len(data):
        if data[i] % 2 ==1:
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
print(find_max_odd([1, 8, 3, 8, 5]))