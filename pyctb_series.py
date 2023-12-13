from datetime import datetime

# f[0] = 1, f[1] = 3, f[2] = 2
def check_thcs(n, f):
    return n == 0 or n == 1 or n == 2

def thcs(n, f):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    elif n == 2:
        return 2

def ctth(n, f):
    return pyctb_series(n-3, f) * (pyctb_series(n-2, f) + pyctb_series(n-1, f))

def check_calculated(n, f):
    return n in f

def memorized(n, f):
    return f[n]

def save(n, f, res):
    f[n] = res

def pyctb_series(n, f):
    
    if check_calculated(n, f):
        return memorized(n, f)
    
    else:
    
        # if check_thcs(n, f):
        #     res = thcs(n, f)
        if n == 0:
            return 1
        elif n == 1:
            return 3
        elif n == 2:
            return 2
        else:
            res = ctth(n, f)
        save(n, f, res)
        return res

start = datetime.now()
n = 4
f = dict()
print(pyctb_series(n, f))
end = datetime.now()
print(end - start)