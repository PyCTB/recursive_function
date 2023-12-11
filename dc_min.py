
def check_thcs(a):
    if len(a) == 1:
        return True
    else:
        return False
    # return len(a) == 1

def thcs(a):
    return a[0]

def ctth(a):
    mp = len(a) // 2
    rl = dc_min(a[:mp])
    rr = dc_min(a[mp:])
    return min(rl, rr)

def dc_min(a):
    if check_thcs(a):
        res = thcs(a)
    else:
        res = ctth(a)
    return res

x = [3, -2, 1, 7, -5]
r = dc_min(x)

print(r)