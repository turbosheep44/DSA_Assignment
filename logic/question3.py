


def findExtremes(a):
        extremePoints = []

        for x in range(1, len(a) - 1):
                if not (a[x-1] < a[x] < a[x+1]):
                        extremePoints.append(x)

        return extremePoints

if __name__ == '__main__':
        a = [12,19,23,45,64,72,88,95,405,523,662,684] 
        extremes = findExtremes(a)
        for p in extremes:
                print("extreme point at index :", p)
        if len(extremes) == 0:
                print("list is sorted")
