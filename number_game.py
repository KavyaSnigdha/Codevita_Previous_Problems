
def prime(n):
    i = 2
    factors = []
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
            
n=int(input())
l=[]

l=list(map(int,input().split(" ")))

d=[0]*len(l)
for j in range(len(l)):
    d[j]+=len(prime(l[j]))
k=d


su=0
for a in range(len(k)):
    su=su^k[a]
if su==0:
    print("JASBIR")
else:
    print("AMAN")
        
            
            

    
