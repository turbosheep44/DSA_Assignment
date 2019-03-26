import random

# creates a random array with the given length (256 if this is unspecified)
# the array is populated with numbers in the range min - max, endpoints included 
def randomArray(min = 0, max = 1024, length = 256):
    # if the parameters were passed badly (i.e. max is smaller than min) then swap them
    if max < min:
        temp = min
        min = max
        max = temp
    
    # create the empty array
    array = []

    # iterate 'length' times; use abs to ensure safety if a negative length is passed
    for x in range(abs(length)):
        # each time add a new random integer to the array
        array.append(random.randint(min, max))

    # return the new array
    return array

def arrayN(n):
    r = []
    for i in range(1, n+1):
        r.append(i)
    return r