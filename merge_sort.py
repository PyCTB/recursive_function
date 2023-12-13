import numpy as np

def check_thcs(a):
    return len(a) <= 1

def thcs(a):
    return a

def ctth(a):
    
    # Divide
    mp = len(a) // 2
    _al = a[:mp]
    _ar = a[mp:]
    
    # Conquer
    ## Giai bai toan con
    al = merge_sort(_al)
    ar = merge_sort(_ar)
    
    ## Ket hop loi giai
    res = []
    il = ir = 0
    while il < len(al) and ir < len(ar):
        if al[il] < ar[ir]:
            res.append(al[il])
            il += 1                 # il = il + 1
        else:
            res.append(ar[ir])
            ir +=1                  # ir = ir + 1
    if il >= len(al):
        res += ar[ir:]
    else:
        res += al[il:]
    return res

def merge_sort(a):
    if check_thcs(a):
        res = thcs(a)
    else:
        res = ctth(a)
    return res

a = (np.round(np.random.random(10) * 100)).tolist()
print(a)
res = merge_sort(a)
print(res)