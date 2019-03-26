


def getDuplicates(list):
    # create an empty dictionary (hash table) that will store whether or not a variable has been found in the list previously
    dictionary = {}
    # an empty list which will contain all the duplicates in the list
    duplicates = []

    # loop through each element in the list
    for x in list:
        # if the element has appeared before in the list (i.e. exists in the dictionary)
        if x in dictionary:
            # then increment the value in the dictionary for this element
            dictionary[x] += 1

        # add an entry to the dictionary for this element
        else :
            dictionary[x] = 1
    
    # now go through every value in the dictionary
    for key in dictionary:
        # check if there was more than one instance of this element
        if dictionary[key] > 1 :
            # if so add it to the duplicates list
            duplicates.append(key)

    # return the list of duplicates
    return duplicates

    
def getDuplicatesAlt(list):
    # create an empty dictionary (hash table) that will store whether or not a variable has been found in the list previously
    dictionary = {}
    # an empty list which will contain all the duplicates in the list
    duplicates = []

    # loop through each element in the list
    for x in list:
        # if the element has appeared before in the list (i.e. exists in the dictionary)
        if x in dictionary and x not in duplicates:
            duplicates.append(x)
        else:
            dictionary[x] = True

    # return the list of duplicates
    return duplicates

# note that lookups in the dictionary have time complexity of O(1) since dictionaries 
# in python are implemented as hash tables
#       source : https://docs.python.org/3/faq/design.html#how-are-dictionaries-implemented-in-cpython
# this is confirmated also at 
#       https://wiki.python.org/moin/TimeComplexity

# also, the second loop has a time complexity of O(n) where n is the number of unique value in the list
# this is known since iteration of a dictionary in python has time complexity of O(n)
#       source : https://wiki.python.org/moin/TimeComplexity



# an alternative implementation would be to use the following if statement in the first for loop and 
# remove the second for loop altogether

#       if x in dictionary and x not in duplicates:
#           duplicates.append(x)
#       else:
#           dictionary[x] = True

# although this was discarded since then in each iteration of the loop, the 'x not in duplicates' statement
# would iterate through every duplicate that has been found so far with time complexity O(n)
# for a large data set with many duplicates this would makes the program a great deal slower than simply collecting 
# all the duplicates at the end, which is the implementation of choice above

if __name__ == '__main__':
    import tools
    import timeit

    array = tools.randomArray(1, 100, length=10000)

    s = timeit.timeit(lambda: getDuplicates(array), number=1000)
    print("Time taken by algorithm A (proposed solution): ")
    print("\t", s)

    a = timeit.timeit(lambda: getDuplicatesAlt(array), number=1000)
    print("Time taken by algorithm B (alternative solution): ")
    print("\t", a)