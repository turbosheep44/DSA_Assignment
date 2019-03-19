import timeit

def sumFibonnaciAlt(n):
    t = [1, 1]

    for x in range(2, n):
        t.append(t[x-1] + t[x-2])

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
    for i in range(2, n):
        #calculate the next value in the series
        new = current + previous
        # add the new value to the total
        total += new
        # make the previous value the current value
        previous = current
        # make the current value the new value
        current = new
        

    return total

print("memory efficient")
print(sumFibonnaci(400))
print(timeit.timeit(lambda: sumFibonnaci(400), number=100000))
print("alternative")
print(sumFibonnaciAlt(400))
print(timeit.timeit(lambda: sumFibonnaciAlt(400), number=100000))
