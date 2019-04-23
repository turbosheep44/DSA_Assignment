def solution(ranks):
    # create a dictionary of ranks
    rankDictionary = {}

    # add each rank to the dictonary
    for rank in ranks:
        if rank in rankDictionary:
            rankDictionary[rank] += 1
        else:
            rankDictionary[rank] = 1

    # a variable storing the number of soldiers that have a superior to report to
    total = 0

    # go through every rank (key) in the dictionary
    for rank in rankDictionary.keys():
        # add the subordinates of this rank (if there are any) to the total
        if rank - 1 in rankDictionary:
            total += rankDictionary[rank - 1]

    # return the total
    return total


print(solution([4,4,3,3,1,0]))