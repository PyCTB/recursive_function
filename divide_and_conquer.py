
def dc_sum(a):
    print('Tinh tong mang:', a)
    if len(a) == 1:
        res = a[0]
    else:
        mp = len(a) // 2
        res = dc_sum(a[:mp]) + dc_sum(a[mp:])
    print('Tong mang', a, ' la:', res)
    return res
    
x = [1, 2, 3, 4, 5, 6, 7]
s = dc_sum(x)

print(s)