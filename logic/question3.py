
a = [3, 7, 9, 23, 56, 76, 99, 333, 1243, 6565]

sorted = True

for x in range(1, len(a) - 1):
    if not (a[x-1] < a[x] < a[x+1]):
        print("Extreme point found ", a[x])
        sorted = False

if sorted:
    print("SORTED LIST")
