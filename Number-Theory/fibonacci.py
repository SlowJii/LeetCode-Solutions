import math

def is_fibonacci(n) -> bool:
    if n < 0: 
        return False
    if n == 0 or n == 1:
        return True
    expr1 = 5 * n * n + 4
    expr2 = 5 * n * n - 4

    sqrt1 = int(math.sqrt(expr1))
    sqrt2 = int(math.sqrt(expr2))

    return sqrt1*sqrt1 == expr1 or sqrt2*sqrt2==expr2

input = int(input())
for i in range(1, input + 1):
    if is_fibonacci(i) == True:
        print(i)
