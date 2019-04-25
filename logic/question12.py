

def sumFibonnaciAlt(n):
    t = [1, 1]

    for x in range(2, n):
        t.append(t[x-1] + t[x-2])

    #print(sys.getsizeof(t))
    return sum(t)

def sumFibonnaci(n):
    # if the user wants the 1st or 2nd element sum we can return them 
    # directly since it is known that the series start with 1, 1
    if n == 1:
        return 1
    elif n == 2:
        return 2 

    # otherwise, start from a total of 2, since the program begins iterating from n = 2
    total = 2

    # these variables are used to move through the series 
    current = 1
    previous = 1
    new = 0

    # starting from 2 since we have already set the total to 2 
    # since it is known that the series starts with 1, 1
    for _ in range(2, n):
        #calculate the next value in the series
        new = current + previous
        # add the new value to the total
        total += new
        # make the previous value the current value
        previous = current
        # make the current value the new value
        current = new
        
    return total
    
if __name__ == '__main__':
    import timeit
    import sys
    print("memory efficient")
    print(sumFibonnaci(6000))
    print(timeit.timeit(lambda: sumFibonnaci(4), number=1000))
    print("alternative")
    print(sumFibonnaciAlt(6000))
    print(timeit.timeit(lambda: sumFibonnaciAlt(6000), number=1000))

