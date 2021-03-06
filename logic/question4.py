if __name__ == '__main__':
    import tools 
else:
    import logic.tools as tools

# takes a list of integers to search for the possible 2-pairs with the same product
def findPairs(l):
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

    # remove the number 0, problematic because for all numbers, 0 creates a matching product
    # and violates a != b != c != d
    l.remove(0)

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
    #print(len(output))
    return output

# test stub
#array = tools.randomArray(1, 1024, 100)
#print("original array : ", array)
#print(*main(array), sep="\n")
if __name__ == '__main__':
    import timeit
    array = [12,4,5,3,6,8,33,55,11,4,6,78,19,22]
    print(findPairs(array))
        
