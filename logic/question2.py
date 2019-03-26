


def merge(a, b):
    r = []

    while len(a) != 0 and len(b) != 0:
        if a[0] > b[0]:
            r.append(b.pop(0))
        else:
            r.append(a.pop(0))

    if len(a) == 0:
        r.extend(b)
    else:
        r.extend(a)

    return r


if __name__ == '__main__':
    a = [3, 7, 9, 23, 56, 76, 98, 333, 1243, 6565]
    b = [5, 6, 9, 17, 19, 25, 45, 67, 78, 99, 201, 5353, 8987, 23947, 2309487, 43057025]
    c = merge(a, b)
    print(c)
