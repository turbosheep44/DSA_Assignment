

# the merge sort algorithm
# accepts two (sorted) arrays and returns a third, merged list made from these arrays
# the method also accepts an argument 'asc' that should be set to false if the arrays 
# are not sorted in ascending order
def merge(a, b, asc=True):
    # create the new array to merge the argument arrays into
    r = []

    # if the arrays are ascending use the greater than comparison
    if asc:
        compare = lambda x, y:  x > y
    # otherwise, compare using a less than operator
    else:
        compare = lambda x, y:  x < y

    # if either of the arrays has no items remaining we can stop this part of the algorithm
    while len(a) != 0 and len(b) != 0:
        # if the smaller/larger element (found at index zero in each array) is found in array b
        # add this element to the end of the new list 'r' and remove it from b
        if compare(a[0], b[0]):
            r.append(b.pop(0))
        # otherwise, add the first element to array a to the list r and remove the first element 
        # from array a
        else:
            r.append(a.pop(0))

    # if the above algorithm completed because there were no more elements in list a
    # append the remaining elements of list b to the return list
    if len(a) == 0:
        r.extend(b)
    # otherwise, append the remaining elements of list a to the return list
    else:
        r.extend(a)
    
    # return the merged lists 
    return r


if __name__ == '__main__':
    a = [-19,-12,-8,-1,3, 7, 9, 23, 56, 76, 98, 333, 1243]
    b = [-15,-12,-5,-2,2,5, 6, 9, 17, 19, 25, 45, 67, 78]
    print()
    print(a)
    print(b)
    c = merge(a, b)
    print(c)
    print()
