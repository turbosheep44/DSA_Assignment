
def sumFibonnaci(n):
    t = [1, 1]

    for x in range(2, n):
        t.append(t[x-1] + t[x-2])

    return sum(t)


print(sumFibonnaci(5))
