import numpy as np

def check_thcs(a):
    return len(a) <= 1

def thcs(a):
    return a

def ctth(a):
    
    # Divide
    _al = []
    _ar = []
    pivot = (max(a) + min(a)) / 2
    for i in a:
        if i < pivot:
            _al.append(i)
        else:
            _ar.append(i)
    
    # Conquer
    ## Giai bai toan con
    al = quick_sort(_al)
    ar = quick_sort(_ar)
    
    ## Ket hop loi giai
    res = al + ar
    
    return res

def quick_sort(a):
    if check_thcs(a):
        res = thcs(a)
    else:
        res = ctth(a)
    return res

a = (np.round(np.random.random(10) * 100)).tolist()
print(a)
res = quick_sort(a)
print(res)