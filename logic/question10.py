

def findLargest(list):
    #   base case
    # the largest item in a list with one element is that one item
    if len(list) == 1:
        return list[0]

    #    recursive case
    # take the last number in the list
    n = list.pop()
    # recursiveley find the largest number in the rest of the list
    largest = findLargest(list)
    
    # if n is largest than the largest number in the rest of the list 
    # it must be the largest overall, so return n
    if n > largest:
        return n
    # otherwise return the largest number found so far
    else:
        return largest

if __name__ == '__main__':
    import tools
    array = [-4,2.34,-1,-18,3.141,9.2]
    print()
    print(array)
    print("the largest number is: ", findLargest(array))
    print()