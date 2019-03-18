import random

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
    
    


        



# seed the random number generator using the system time
random.seed()

# initialise two arrays
a = []
b = []

# populate the arrays with random numbers
length = random.randint(256, 512)
for x in range(length):
    a.append(random.randint(0, 1024))

length = random.randint(256, 512)
for x in range(length):
    b.append(random.randint(0, 1024))

print("--------------- Array A -----------------")
print(a)
print("--------------- Array B -----------------")
print(b)

quicksort(b)

print("--------------- Sorted Array B -----------------")
print(b)
print("Done")
