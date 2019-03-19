
def main(list):
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

    
def mainAlt(list):
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

import timeit

s = timeit.timeit(lambda: main([1, 4, 5, 5, 6, 7, 7, 10, 13, 14, 15, 18, 18, 20, 21, 21, 22, 22, 23, 23, 23, 23, 25, 25, 26, 27, 27, 27, 28, 28, 28, 29, 29, 30, 30, 34, 34, 35, 36, 38, 43, 43, 45, 47, 47, 48, 48, 49, 50, 50, 51, 52, 53, 53, 53, 53, 53, 53, 55, 56, 56, 57, 58, 58, 58, 58, 59, 59, 60, 61, 61, 61, 63, 64, 65, 65, 68, 70, 71, 73, 74, 74, 74, 74, 75, 78, 79, 79, 81, 81, 82, 83, 83, 87, 89, 90, 91, 91, 94, 94, 95, 95, 96, 99, 99, 102, 103, 104, 105, 105, 105, 106, 106, 107, 107, 109, 111, 112, 113, 114, 114, 120, 122, 123, 123, 124, 124, 125, 125, 128, 128, 129, 130, 131, 133, 133, 135, 136, 136, 137, 138, 139, 139, 139, 144, 144, 145, 147, 147, 147, 148, 149, 150, 150, 150, 151, 151, 151, 154, 155, 156, 162, 162, 162, 167, 168, 171, 171, 175, 177, 177, 177, 177, 181, 181, 181, 181, 182, 183, 185, 186, 194, 198, 198, 200, 200, 200, 200, 200, 201, 202, 202, 202, 206, 207, 207, 209, 210, 210, 210, 211, 212, 213, 213, 214, 215, 216, 216, 217, 218, 221, 222, 223, 225, 225, 226, 227, 230, 230, 234, 234, 234, 236, 237, 239, 240, 242, 243, 243, 244, 245, 246, 246, 247, 247, 248, 249, 252, 253, 253, 254, 254, 257, 257, 258, 260, 260, 263, 263, 264, 264, 265, 266, 267, 268, 268, 269, 270, 270, 271, 271, 272, 272, 275, 275, 276, 279, 281, 282, 284, 285, 286, 286, 287, 288, 291, 296, 296, 297, 297, 297, 298, 298, 298, 299, 303, 304, 306, 306, 308, 310, 310, 311, 312, 312, 313, 314, 316, 316, 316, 316, 317, 317, 320, 320, 320, 322, 322, 323, 325, 326, 326, 326, 327, 329, 330, 330, 330, 333, 333, 334, 334, 334, 335, 336, 336, 337, 337, 339, 339, 340, 340, 341, 342, 343, 343, 343, 343, 343, 346, 347, 350, 350, 356, 358, 358, 359, 360, 360, 360, 360, 363, 363, 363, 363, 365, 369, 370, 371, 372, 373, 373, 377, 377, 377, 377, 377, 378, 380, 381, 381, 381, 381, 382, 382, 382, 383, 384, 385, 388, 390, 391, 391, 391, 392, 393, 394, 396, 398, 398, 399, 399, 399, 400, 400, 402, 403, 403, 404, 404, 406, 408, 408, 411, 413, 413, 413, 413, 414, 416, 416, 418, 418, 421, 422, 423, 424, 425, 425, 425, 426, 427, 428, 429, 432, 433, 433, 434, 435, 435, 437, 437, 437, 437, 438, 440, 440, 441, 443, 443, 444, 444, 444, 445, 446, 447, 450, 454, 456, 456, 456, 457, 457, 457, 459, 460, 461, 461, 462, 464, 465, 465, 465, 467, 467, 467, 468, 469, 470, 473, 473, 473, 473, 474, 474, 476, 478, 479, 480, 481, 482, 483, 484, 484, 484, 485, 485, 486, 487, 487, 487, 488, 488, 491, 493, 494, 494, 494, 499, 500]))
print("Time taken by algorithm A (proposed solution): ")
print("\t", s)

a = timeit.timeit(lambda: mainAlt([1, 4, 5, 5, 6, 7, 7, 10, 13, 14, 15, 18, 18, 20, 21, 21, 22, 22, 23, 23, 23, 23, 25, 25, 26, 27, 27, 27, 28, 28, 28, 29, 29, 30, 30, 34, 34, 35, 36, 38, 43, 43, 45, 47, 47, 48, 48, 49, 50, 50, 51, 52, 53, 53, 53, 53, 53, 53, 55, 56, 56, 57, 58, 58, 58, 58, 59, 59, 60, 61, 61, 61, 63, 64, 65, 65, 68, 70, 71, 73, 74, 74, 74, 74, 75, 78, 79, 79, 81, 81, 82, 83, 83, 87, 89, 90, 91, 91, 94, 94, 95, 95, 96, 99, 99, 102, 103, 104, 105, 105, 105, 106, 106, 107, 107, 109, 111, 112, 113, 114, 114, 120, 122, 123, 123, 124, 124, 125, 125, 128, 128, 129, 130, 131, 133, 133, 135, 136, 136, 137, 138, 139, 139, 139, 144, 144, 145, 147, 147, 147, 148, 149, 150, 150, 150, 151, 151, 151, 154, 155, 156, 162, 162, 162, 167, 168, 171, 171, 175, 177, 177, 177, 177, 181, 181, 181, 181, 182, 183, 185, 186, 194, 198, 198, 200, 200, 200, 200, 200, 201, 202, 202, 202, 206, 207, 207, 209, 210, 210, 210, 211, 212, 213, 213, 214, 215, 216, 216, 217, 218, 221, 222, 223, 225, 225, 226, 227, 230, 230, 234, 234, 234, 236, 237, 239, 240, 242, 243, 243, 244, 245, 246, 246, 247, 247, 248, 249, 252, 253, 253, 254, 254, 257, 257, 258, 260, 260, 263, 263, 264, 264, 265, 266, 267, 268, 268, 269, 270, 270, 271, 271, 272, 272, 275, 275, 276, 279, 281, 282, 284, 285, 286, 286, 287, 288, 291, 296, 296, 297, 297, 297, 298, 298, 298, 299, 303, 304, 306, 306, 308, 310, 310, 311, 312, 312, 313, 314, 316, 316, 316, 316, 317, 317, 320, 320, 320, 322, 322, 323, 325, 326, 326, 326, 327, 329, 330, 330, 330, 333, 333, 334, 334, 334, 335, 336, 336, 337, 337, 339, 339, 340, 340, 341, 342, 343, 343, 343, 343, 343, 346, 347, 350, 350, 356, 358, 358, 359, 360, 360, 360, 360, 363, 363, 363, 363, 365, 369, 370, 371, 372, 373, 373, 377, 377, 377, 377, 377, 378, 380, 381, 381, 381, 381, 382, 382, 382, 383, 384, 385, 388, 390, 391, 391, 391, 392, 393, 394, 396, 398, 398, 399, 399, 399, 400, 400, 402, 403, 403, 404, 404, 406, 408, 408, 411, 413, 413, 413, 413, 414, 416, 416, 418, 418, 421, 422, 423, 424, 425, 425, 425, 426, 427, 428, 429, 432, 433, 433, 434, 435, 435, 437, 437, 437, 437, 438, 440, 440, 441, 443, 443, 444, 444, 444, 445, 446, 447, 450, 454, 456, 456, 456, 457, 457, 457, 459, 460, 461, 461, 462, 464, 465, 465, 465, 467, 467, 467, 468, 469, 470, 473, 473, 473, 473, 474, 474, 476, 478, 479, 480, 481, 482, 483, 484, 484, 484, 485, 485, 486, 487, 487, 487, 488, 488, 491, 493, 494, 494, 494, 499, 500]))
print("Time taken by algorithm B (alternative solution): ")
print("\t", a)