'''def factorial(p):
    fact=[0]*p
    fact[0]=1
    fact[1]=1
    for i in range(2,p+1):
        k=i*fact[i-1]
        fact.insert(i,k)
        
    return fact[p]'''
    
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

'''def prime(n):
    d=dict()
    d[2]=0
    while n % 2 == 0:
        d[2]+=1
        n = n // 2
  
    for i in range(3,int(n**0.5)+1,2):
        count=0
        while n % i== 0:
            count+=1
            d[i]=count
            n = n // i
   # if n is a prime
    if n > 2:
        d[n]+=1
    for k in d.keys():
        print(d.get(k),end=" ")'''
            

n=input()

if int(n)<0:
    print("Invalid Input")
    
elif not n.isdigit():
    print("Invalid Input")
    
else:
    n=int(n)
    
    d=[]
    for k in range(2,n+1):
        d.extend(prime(k))
    k=d
    l=[0]*max(k)
    
    for i in range(len(k)):
        l[k[i]-1]+=1
        
    for i in l:
        if i!=0:
            print(i,end=" ")
