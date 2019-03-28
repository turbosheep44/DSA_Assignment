

"""
    We can eliminate and devisors greater than sqrt(n) since if  a*b = n, and a > sqrt(n) then b < sqrt(b), otherwise a*b > n. 
    So, by testing all divisors smaller than or equal to sqrt(n), we can eliminate the need to test any divisors greater than sqrt(n), effectively 
    halving the time taken to check primality.

    Observe that, all primes are of the form 6k ± 1, with the exception of 2 and 3. This is because all integers can be expressed as (6k + i) 
    for some integer k and for i = −1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3). 

    So, a more efficient method is to test if n is divisible by 2 or 3, and if it is not, then to check through all the numbers of form 6k ± 1 
    This is 3 times as fast as testing divisibility with all numbers less than sqrt(n)
"""


def primeCheck(n):
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

def firstTenK():
    for i in range(104730):
        primeCheck(i)



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
def sieve(n):
    # this is an array of booleans, where the index represents the actual integer being checked
    # and the value represents whether it is a prime number or not
    # we start by assuming that all the numbers in the range are prime i.e. the element has a value True
    numbers = [True] * (n + 1)

    #t the numbers 0 and 1 are not prime so remove them before starting
    numbers[0] = numbers[1] = False

    # iterating through each of the elements in the list 
    for i in range(len(numbers)):
        # if the value in the array is still True, then it must be a prime and 
        # so the program will remove all its multiples [1]
        if numbers[i]:
            # removing all multiples of this prime [2]
            for multiple in range(i**2, len(numbers), i):
                numbers[multiple] = False

    # now iterate through the list and collect all the primes in a new array
    primes = []
    for i in range(len(numbers)):
        if numbers[i]:
            # add the primes to the list
            primes.append(i)

    return primes


if __name__ == '__main__':
    import timeit
    #print(timeit.timeit(firstTenK, number=100)/100)
    #print(timeit.timeit(lambda: sieve(10000), number=1))

    primes = sieve(36)
    print(primes)
    print(len(primes))
    #print(timeit.timeit(lambda: sieve(1000), number=1))




