import random
import timeit
import logic.tools as tools

# quicksotrting a partial list
# if the range of list indices are not defined then use the start and end of the list
# i.e. sort the whole list
def quicksort(list, left = 0, right = None):
    
    #if the right pointer is not set the make it the end of the list
    if right == None:
        right = len(list) - 1

    # if the difference between the pointers is less than one then return since
    # a single element list is already sorted
    if right - left  < 1:
        return list

    # choose the first element in the list as the pivot
    pivot = left
    # increment the left pointer so we dont start from the pivot 
    left += 1

    # define the bounds of the sort we are performing
    extremeLeft = pivot
    extremeRight = right

    while True:
        # increment the left pointer until we reach a value that is larger then the pivot
        # also make sure we do not overstep the sorting bounds
        while list[left] < list[pivot] and left < extremeRight:      
            left += 1
        
        # then decrement the list until a value smaller than the pivot is found
        # also make sure we do not overstep the sorting bounds
        while list[right] >= list[pivot] and right > extremeLeft:
            right -= 1

        # if the pointers have not yet met then swap the values at the left and right pointers
        if right > left:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp
        # if the pointers have crossed over, then swap with the right pointer with the pivot
        else:
            temp = list[right]
            list[right] = list[pivot]
            list[pivot] = temp
            # then, now that the array has been partitioned, used recursion to sort each partition 
            # note that we use 'right' here instead of pivot since the index of right is now where
            # the pivot is
            quicksort(list, extremeLeft, right - 1)
            quicksort(list, right + 1, extremeRight)
            return
    

# the shell sort algorithm
def shellsort(list):
    # separation is number of elements in the actual list between elements in the sublist
    # the first iteration of the shell sort will contain lists with 2 items
    separation = len(list) // 2

    while separation > 1:
        # for any separation value we must sort that number of sub lists where the first 
        # element of each sub list goes from 0 to n
        # e.g. for a separation value of 4, we sort 4 sub lists that start from indices 0, 1, 2 and 3
        for i in range(separation):
            nSort(list, i, separation)
        # half the separation value
        separation = separation // 2
    
    # once the separation value reaches one, iterate once more before finishing
    nSort(list, 0, 1)

        
# performs an insertion sort on a list but only sorts indices that are step elements apart
# starting from the given start index
def nSort(list, start, step):
    shiftPointer = 0
    # for each index starting from 'start', until the end of the list which are separated by 'step'
    for i in range(start, len(list), step):
        # get the current value (that we are inserting)
        current = list[i]

        # start at the previous position
        shiftPointer = i - step
        # repeatedly shift until the program finds a value that is smaller than the current value
        # or until the program readches an invalid (negative) index
        while shiftPointer >= 0 and list[shiftPointer] > current:
            list[shiftPointer + step] = list[shiftPointer]
            shiftPointer -= step
        # once we have found a value that is smaller than the current value or reached the 
        # beginning of the array, put the current value in the previous slot
        list[shiftPointer + step] = current


def qTest():
    a = tools.randomArray(length = 3000)
    quicksort(a[:])

def sTest():
    a = tools.randomArray(length = 3000)
    shellsort(a[:])

if __name__ == '__main__':
    print(timeit.timeit(qTest, number=10))
    print(timeit.timeit(sTest, number=10))
