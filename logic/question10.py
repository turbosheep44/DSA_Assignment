

def findLargest(list):
    #   base case
    # the largest item in a list with one element is that one item
    if len(list) == 1:
        return list[0]

    #    recursive case
    # take the last number in the list
    n = list.pop()
    # recursiveley find the last number in the rest of the list
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
    array = [12,15,16,21,35,21,64,38,65,32,95,54,61,2,4,6,9,35,74]
    print()
    print(array)
    print("the largest number is: ", findLargest(array))
    print()