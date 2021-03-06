
"""
    cos(x) = SUMMATION [  {(-1^k)/(2k!)}x^2k  ]
    sin(x) = SUMMATION [  {(-1^k)/(2k+1)!}x^(2k+1)  ]
"""

from math import pi

# a factorial method is needed since the denominator in each case is a factorial
def factorial(n):
    # base case
    if n == 0:
        # 0! = 1
        return 1

    # recursive case, n! = n * (n-1)!
    return n * factorial(n-1)

# the cosine method, where n is the number of iterations and r is the cosine argument in radians
def cosine(r, n = 120):
    # normalise argument
    r = normaliseArgument(r)

    # start the initial value at 0
    value = 0

    # perform n iterations
    for i in range(n):
        # in each iterations add to the current value as per the formula
        value += (((-1) ** i)/(factorial(2 * i)))*(r ** (2 * i))
    
    return value

# the sine method, where n is the number of iterations and r is the sine argument in radians
def sine(r, n = 150):
    # normalise argument
    r = normaliseArgument(r)

    # start the initial value at 0
    value = 0

    # perform n iterations
    for i in range(n):
        # in each iterations add to the current value as per the formula
        value += (((-1) ** i)/(factorial((2 * i) + 1)))*(r ** ((2 * i) + 1))
    
    return value

# a method that takes any argument and returns an argument (t)
# such that cos(t) = cos(r) and sin(t) = sin(r)
# and also, 0 < t < 2*pi
def normaliseArgument(r):
    return abs(r % (pi * 2))

if __name__ == '__main__':
    import math
    test = 7.7
    print(sine(test))
    print(math.sin(test))
    print(sine(test)-math.sin(test))
