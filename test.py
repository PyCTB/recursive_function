
def dp_sum(a, i):
    print('Dang tinh tong mang:', a[:(i+1)])
    res = dp_sum(a, i-1) + a[i]
    return res
    
x = [1, 2, 3, 4, 5, 6 , 7]
n = len(x) - 1
s = dp_sum(x, n)

print(s)