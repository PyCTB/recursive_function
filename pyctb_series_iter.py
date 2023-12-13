from datetime import datetime
# 1, 1, 2, 3, 5, 8, 13,...
def iterative_fibonaci(n):
    f = [1, 3, 2]
    if n <= 2:
        return f[n]
    else:
        for i in range(3, n+1):
            f.append(f[i-3] * (f[i-1] + f[i-2]))

        return f[n]

start = datetime.now()
print(iterative_fibonaci(4))
end = datetime.now()
print(end - start) # 0:00:00.012996