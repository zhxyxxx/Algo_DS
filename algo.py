# GCD
def gcd(a, b) -> int:
    if a < b:
        buf = b
        b = a
        a = buf
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


# binary search
def bi_search(query, key) -> int:
    length = len(query)
    l = 0
    r = length-1
    ans = -1
    while True:
        if l > r:
            break
        m = (l+r)//2
        if query[m] > key:
            r = m-1
        elif query[m] < key:
            l = m+1
        else:
            ans = m
            break
    return ans


def selection_sort(query):
    length = len(query)
    for i in range(length):
        min_i = i
        for j in range(i+1, length):
            if query[j] < query[min_i]:
                min_i = j
        query[i], query[min_i] = query[min_i], query[i]
    return query


def insertion_sort(query):
    length = len(query)
    for i in range(1, length):
        j = i-1
        v = query[i]
        while query[j] > v and j >= 0:
            query[j+1] = query[j]
            j -= 1
        query[j+1] = v
    return query


def bubble_sort(query):
    length = len(query)
    for i in range(length-1):
        for j in range(i, -1, -1):
            if query[j] > query[j+1]:
                query[j], query[j+1] = query[j+1], query[j]
    return query

