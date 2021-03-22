# GCD
def GCD(a, b) -> int:
    if a < b:
        buf = b
        b = a
        a = buf
    r = a % b
    if r == 0:
        return b
    else:
        return GCD(b, r)

# binary search
def bisearch(list, key) -> int:
    length = len(list)
    l = 0
    r = length-1
    ans = -1
    while True:
        if l > r:
            break
        m = (l+r)//2
        if list[m] > key:
            r = m-1
        elif list[m] < key:
            l = m+1
        else:
            ans = m
            break
    return ans
