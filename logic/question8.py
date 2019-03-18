
# 415

# To find the square root of n, we find the value of x that satisfies x^2 = n
#     =>  0 = x^2 - n
# Thus we find the value of x for which y is 0 (the root) of the equation
#         y = x^2 - n
# This can be done using the newton raphson method; where
#         f(x) = x^2 - n
#     =>  f'(x) = 2x
#
# The newton raphson method uses:
#     x(n+1) = xn - f(x)/f'(x)

# a method to calculate f(x) for any value of x

import math

PATTERN = "pattern"
PATTERN_EXISTS = "patternFound"
ITERATIONS = "iterations"
SOLUTION = "sqrt"

def f(x, n):
    return x**2 - n

# a method to calculate f'(x) for any value of x


def fPrime(x):
    return 2 * x

# attempts to find some pattern in the list
# returns true if a pattern is found


def patternCheck(list):
    # a list to store the pattern while we are trying to detect a pattern
    pattern = []
    # first begin by taking the first value in the list
    pattern.append(list.pop(0))

    # a variable to get the hold the next value in the list temporarily
    next = None

    halfLen = math.ceil(len(list)/2)

    # this loop should continue until we remove half of the list
    # (or it may break when we return from inside the loop)
    while len(list) != halfLen:
        # get the next value in the list
        next = list.pop(0)

        # if the new value does not match the first value in the pattern,
        # then we have not found the start of the pattern repeating so append
        # it to the pattern
        if next != pattern[0]:
            pattern.append(next)
        # however, if we match with the first element of the pattern we have
        # potentially found the start of a repeat
        else:
            # in this case check every other element of the list and continue
            # matching it with the pattern
            current = 1
            for i in range(0, len(list)):
                if current == len(pattern):
                        current = 0

                if pattern[current] == list[i]:
                    current += 1
                    
                    # if we manage to get to the end of the list, a pattern has been found so return true
                    if i == len(list) - 1:
                        return True
                # if we fail to match at some point, simply append the next value to the list
                else:
                    pattern.append(next)

    return False

def main(n):
    # in order to find a good first guess, we will find the smallest square that is
    # larger than the value we are trying to find
    firstGuess = 1
    while firstGuess ** 2 < n:
        firstGuess += 1

    # this is the number of iterations that we have currently done
    iterations = 0
    # this is the current value of the guess
    x = firstGuess
    # this stores the next value temporarily so that we can safely
    # use x for calculations
    xNext = None
    # this is the list of the last few values of x that were generated
    # and will be used to check that we are not oscilating between some
    # set of values for example 0.00002, 0.000019, 0.00002, 0.000019
    previousValues = []
    previousValues.append(x)

    # now we repeatedly iterate until either:
    #   we perform 1000 iterations
    #   the exact value is found
    #   the value of x is no longer changing
    while iterations < 1000 and x ** 2 != n and not patternCheck(previousValues[:]):
        # use the formula to get the next value of x
        xNext = x - (f(x, n) / fPrime(x))
        # the new vaue of x replaces the old one
        x = xNext
        # add the new value of x to the list
        previousValues.append(x)
        # keep this list less than 8 values long so we dont waste memory
        # if we end up performing many iterations
        if len(previousValues) > 8:
            previousValues.pop(0)
        # record this iteration
        iterations += 1

    # if the iterations ended because of a pattern, choose which value in
    # the pattern is closes to out answer by calculating x^2 for each value
    # and check which one is closest to n
    closest = x
    patternFound = False
    if iterations < 1000 and x ** 2 != n:
        patternFound = True
        closestDifference = 100
        newDifference = None
        for candidate in previousValues:
            newDifference = (candidate ** 2) - n
            if closestDifference > newDifference:
                closest = candidate
                closestDifference = newDifference

    # return values now that we are finished
    return {SOLUTION : closest, ITERATIONS: iterations, PATTERN_EXISTS : patternFound, PATTERN : previousValues}
