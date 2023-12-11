
def dp_sum(a, i):
    if i == 0:
        res = a[i]
    else:
        res = dp_sum(a, i-1) + a[i]
    return res

def check_thcs(a, i):
    return i == 0

def thcs(a, i):
    return a[i]

def ctth(a, i):
    tmp = dp_min(a, i-1)
    if tmp < a[i]:
        return tmp
    else:
        return a[i]
    # <=> return tmp if tmp < a[i] else a[i]      C: tmp < a[i] ? tmp : a[i]    excel: if(tmp < a[i], tmp, a[i])
    # <=> return min(dp_min(a, i-1), a[i])

# dp_min(a, i) -> R_i
def dp_min(a, i):
    if check_thcs(a, i):
        res = thcs(a, i)
    else:
        res = ctth(a, i)
    return res

def dp_max(a, i):
    print(f'Bat dau tim gia tri lon nhat trong {i+1} phan tu dau tien')
    if i == 0:
        res = a[i]
    else:
        res = max(dp_max(a, i-1), a[i])
    print(f'Ket thuc tim gia tri lon nhat trong {i+1} phan tu dau tien')
    return res
    
x = [3, -2, 1, 7, 5]
n = len(x) - 1
r = dp_min(x, n)

print(r)