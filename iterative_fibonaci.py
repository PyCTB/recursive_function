from datetime import datetime
# 1, 1, 2, 3, 5, 8, 13,...
def iterative_fibonaci(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        f = [] # f[i] la so fibonaci thu i
        f.append(1)  # i = 0
        f.append(1)  # i = 1
        
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])

        return f[n]

start = datetime.now()
print(iterative_fibonaci(50))
end = datetime.now()
print(end - start) # 0:00:00.012996