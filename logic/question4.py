import tools

# takes a list of integers to search for the possible 2-pairs with the same product
def main(l):
    # remove duplicates in the list 

    # the following operation has a time compelxity of O(n) since iterating over 
    # a list takes O(n) time and inserting each element in the dictionary takes O(1) time
    l = list(dict.fromkeys(l))
    # by removing duplicates from the list we ensure that a≠b≠c≠d holds as long as the 
    # program doesnt choose the same list index for any two of a, b, c or d in the loops below

    # calculate all possible products and store pairs in hash table
    # we must calculate every possible pair of integers in the list
    # this is done with the following nested for loop (time complexity O(n))
    product = 0
    pair = None
    dictionary = {}
    output = []
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            # multiply the two integers
            product = l[i] * l[j]
            # create a tuple from these two integers
            pair = tuple([l[i], l[j]])
            # if this product has been found before, then add to the output list new entries 
            # containing the current pair and every other previous pair found with the same product
            if product in dictionary:
                for otherPair in dictionary[product]:
                    output.append(tuple([pair, otherPair, product]))
                # then add the current pair to the dictionary under the same product entry
                dictionary[product].append(pair)
            # if this is a new product, then add this entry to the dictionary in a new list
            else:
                dictionary[product] = [pair]

    # return the output list 
    return output


# test stub
#array = tools.randomArray(1, 1024, 100)
#print("original array : ", array)
#print(*main(array), sep="\n")

import timeit
print(timeit.timeit(lambda: main([5,28,38,33,18,11,35,13,42,39,47,12,18,34,49,48,1,2,42,28]), number=1000))
