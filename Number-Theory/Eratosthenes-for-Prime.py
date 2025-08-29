import math 

N = 1000000
prime = [1]*N 
prime[0] = 0
prime[1] = 0

def Eratos():
    i = 2
    while i*i <= N:
        if prime[i] == 0:
            i += 1
            continue
        j = i*i
        while j < N:
            prime[j] = 0
            j+=i 
        i += 1

Eratos()
n = int(input())
for i in range(1,n+1):
    if prime[i] == 1:
        print i