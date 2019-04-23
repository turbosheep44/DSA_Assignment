

# a method that returns the indices of extreme points in the given list a
def findExtremes(a):
        # create an empty array
        extremePoints = []

        # if any point between the first and last element are extreme, add it to the list
        for x in range(1, len(a) - 1):
                # check for extremeness 
                if (a[x-1] < a[x] > a[x+1]) or (a[x-1] > a[x] < a[x+1]):
                        # if the point is extreme add it to the list 
                        extremePoints.append(x)
        
        # return the list of extremes
        return extremePoints

# a method that prints all extreme points or prints 'sorted' if there are none
def printExtremes(a):
        # get all the extreme points
        extremes = findExtremes(a)

        # if there are no extreme points, print that the list is sorted and end here
        if len(extremes) == 0:
                print("list is sorted")

        # otherwise, print the extreme points
        for p in extremes:
                print("extreme point at index :", p)

if __name__ == '__main__':
        a = [12,19,23,45,64,72,88,95,405,523,662,684] 
        printExtremes(a)
        
