from datetime import datetime

def check_thcs(n, f):
    return n == 0 or n == 1

def thcs(n, f):
    return 1

def ctth(n, f):
    return recursive_fibonaci(n-2, f) + recursive_fibonaci(n-1, f)

def check_calculated(n, f):
    return n in f

def memorized(n, f):
    return f[n]

def save(n, f, res):
    f[n] = res

def recursive_fibonaci(n, f):
    
    if check_calculated(n, f):
        return memorized(n, f)
    
    else:
    
        if check_thcs(n, f):
            res = thcs(n, f)
        else:
            res = ctth(n, f)
        save(n, f, res)
        return res

start = datetime.now()
n = 1000
f = dict()
print(recursive_fibonaci(n, f))
end = datetime.now()
print(end - start)