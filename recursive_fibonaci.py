from datetime import datetime

def check_thcs(n):
    return n == 0 or n == 1

def thcs(n):
    return 1

def ctth(n):
    return recursive_fibonaci(n-2) + recursive_fibonaci(n-1)

def recursive_fibonaci(n):
    if check_thcs(n):
        res = thcs(n)
    else:
        res = ctth(n)
    return res

start = datetime.now()
print(recursive_fibonaci(50))
end = datetime.now()
print(end - start)