  def fib_rec(n):
    if n== 1 or n== 2 : 
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)
def fib_ite(n):
    f1,f2 = 1, 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    return f2
print(fib_rec(5)+fib_ite(8))

def fact_rec(n):
    if n== 0:
        return 1
    elif n > 0:
        return n * fact_rec(n-1)
    else:
        return -1
def fact_ite(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i 
    return fact
print(fact_ite(5)+fact_rec(8))
