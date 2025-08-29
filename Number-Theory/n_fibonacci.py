import math

def fibo_n (n) -> int:
    if n <= 1:
        return n
    a = 0
    b = 1
    for _ in range(n-1):
        a,b = b, a+b
    return b

n = int(input())
print(f"So fibonacci thu {n}: ", fibo_n(n))