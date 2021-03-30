import heapq


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


def insertion_sort(query, h=1):
    length = len(query)
    for i in range(h, length, h):
        j = i-h
        v = query[i]
        while query[j] > v and j >= 0:
            query[j+h] = query[j]
            j -= h
        query[j+h] = v
    return query


def bubble_sort(query):
    length = len(query)
    for i in range(length-1):
        for j in range(i, -1, -1):
            if query[j] > query[j+1]:
                query[j], query[j+1] = query[j+1], query[j]
    return query


def shell_sort(query):
    length = len(query)
    h = 1
    while h < length:
        h = 3*h + 1
    while h != 1:
        h = h // 3
        query = insertion_sort(query, h)
    return query


def heap_sort(query):
    length = len(query)
    heapq.heapify(query)
    sortl = []
    for i in range(length):
        sortl.append(heapq.heappop(query))
    return sortl


def merge(a, b):
    index = [0, 0]
    la = len(a)
    lb = len(b)
    merged = []
    while True:
        if index[0] >= la:
            merged.extend(b[index[1]:])
            break
        elif index[1] >= lb:
            merged.extend(a[index[0]:])
            break
        if a[index[0]] < b[index[1]]:
            merged.append(a[index[0]])
            index[0] += 1
        else:
            merged.append(b[index[1]])
            index[1] += 1
    return merged


def merge_sort(query):
    length = len(query)
    if length <= 1:
        return query
    mid = length // 2
    a = merge_sort(query[:mid])
    b = merge_sort(query[mid:])
    sortl = merge(a, b)
    return sortl


def partition(a):
    length = len(a)
    pivot = a[-1]
    tail = length-2
    for i in range(length):
        if a[i] >= pivot:
            for j in range(tail, i-1, -1):
                tail -= 1
                if a[j] < pivot:
                    a[i], a[j] = a[j], a[i]
                    break
        if i >= tail:
            mid = tail+1
            break
    a[mid], a[-1] = a[-1], a[mid]
    return mid


def quick_sort(query):
    length = len(query)
    if length <= 1:
        return query
    mid = partition(query)
    query[:mid] = quick_sort(query[:mid])
    query[mid+1:] = quick_sort(query[mid+1:])
    return query


# string comparison
def bf(text: str, pattern: str) -> int:
    lent = len(text)
    lenp = len(pattern)
    for i in range(lent-lenp+1):
        for j in range(lenp):
            if text[i+j] != pattern[j]:
                break
            if j == lenp-1:
                return i
    return -1


def create_table(p):
    i = 0
    j = -1
    length = len(p)
    kmpnext = [-1 for _ in range(length+1)]
    while i < length:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            kmpnext[i] = j
        else:
            j = kmpnext[j]
    return kmpnext


def kmp(text: str, pattern: str) -> int:
    kmpnext = create_table(pattern)
    lent = len(text)
    lenp = len(pattern)
    i = 0
    j = 0
    while i < lent and j < lenp:
        if j == -1 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = kmpnext[j]
    if j == lenp:
        return i-j
    else:
        return -1
