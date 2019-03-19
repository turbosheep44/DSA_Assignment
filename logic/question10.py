import tools

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


print("the largest number is: ", findLargest(tools.randomArray()))