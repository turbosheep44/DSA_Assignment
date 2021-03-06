

def primeCheck(n):
    n = abs(int(n))
    # any number smaller than 2 is not a prime
    # note that 1 ia NOT a prime
    if n < 2:
        return False
    # 2 and 3 are the primes we must check for explicity since they cannot be expressed in the form 6k ± 1
    elif n == 2 or n == 3:
        return True

    # now check if the number is divisible by 2 or 3, if so then it is not a prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    # otherwise begin testing divisors in the form 6k ± 1 but also less than sqrt(n)
    i = 6
    # note that in the qhile loop we check if (i - 1)^2 is less than n because
    # the program still needs to check that divisor even if the value of i has just
    # exceeded the value of sqrt(n)
    while (i - 1) ** 2 <= n:
        if n % (i + 1) == 0 or n % (i - 1) == 0:
            return False
        i += 6

    # if all divisors up to sqrt(n) are checked and none of them divide n with a remainder 0 then n is prime
    return True

"""
    Optimisations:
    [1] Since every number can be decomposed into its prime factors, the program only needs to 
        remove multiples of primes e.g. since 4 has already been removed when multiples of 2 were 
        removed, the algorithm does not bother checking multiples of 4 since they have already 
        been removed

    [2] If we are removing multiples of some prime i, then the program starts from i^2 since 
        every composite number n has a factor less than or equal to sqrt(n)
        This optimisation means that if we are checking numbers up to n we only actually check
        numbers between 2 and sqrt(n)
"""

# the sieve method, where n is the largest number to be checked 
def sieveOld(n):
    n = abs(int(n))
    # this is an array of booleans, where the index represents the actual integer being checked
    # and the value represents whether it is a prime number or not
    # we start by assuming that all the numbers in the range are prime i.e. the element has a value True
    numbers = [True] * (n + 1)

    # the numbers 0 and 1 are not prime so remove them before starting
    numbers[0] = numbers[1] = False

    # iterating through each of the elements in the list 
    for i in range(n + 1):
        # if the value in the array is still True, then it must be a prime and 
        # so the program will remove all its multiples [1]
        if numbers[i]:
            # removing all multiples of this prime [2]
            for multiple in range(i**2, len(numbers), i):
                numbers[multiple] = False

    # now iterate through the list and collect all the primes in a new array
    primes = []
    for i in range(n + 1):
        if numbers[i]: 
            # add the primes to the list
            primes.append(i)

    return primes

# this algorithm uses the same logic as the older version
# however, the syntax is much more pythonic and thus runs approximately twice as fast
def sieve(n):
    n = abs(int(n))
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, (n + 1)):
        if numbers[i]:
            numbers[i*i::i] = [False] * len(numbers[i*i::i])

    return [i for i, v in enumerate(numbers) if v]


if __name__ == '__main__':
    import timeit
    #print(timeit.timeit(firstTenK, number=100)/100)
    #print(timeit.timeit(lambda: sieve(10000), number=1))

    primes = sieve(36)
    print(primes)
    print(len(primes))
    print(timeit.timeit(lambda: sieveOld(1000), number=1000))
    print(timeit.timeit(lambda: sieve(1000), number=1000))




