
def fib(n):
    L = [0,1]
    for i in range(2, n+1):
        L.append(L[i-2] + L[i-1])
    return L

print(fib(30))
    
