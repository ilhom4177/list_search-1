def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i=0
    even=[]
    while i<len(data):
        if data[i]%2==0:
            even.append(data[i])
        i+=1
    if even==[]:
        return -1

    mx = even[0]
    i = 0
    while i < len(even):
        if even[i]>mx:
            mx = [i]
        i += 1

    return mx