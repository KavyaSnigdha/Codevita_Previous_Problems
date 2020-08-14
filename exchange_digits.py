from itertools import permutations
import sys

value,compare=input().split()


compare=int(compare)

a=value
b=compare

if int(a)<1 or b<1 or int(a)>10000000 or b>10000000:
   
    print(-1)

elif len(str(a))<len(str(b)):
    
    print(-1)
    

    
else:
    a=str(a)
    num=list(permutations(a))
    
    
    i=0
    k=[]
    while i<len(num):
        k.append("".join(num[i]))
    
        i+=1
    i=0
    l=[]
    while i<len(k):
        if k[i][0]!='0':
            l.append(int(k[i]))
        i+=1
    
    k=l
    
    num=sorted(list(set(k)))
    Min=-1
    for number in num:
        if number>b:
            Min=number
            break
    print(Min)
