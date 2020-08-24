
def fact(i):
    factorial=[1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000,20922789888000,355687428096000,6402373705728000,121645100408832000,2432902008176640000]
    return(factorial[i])
def ncr(x,y):
    if x==y or y==0:
        return 1
    if y==1:
        return x
    result=fact(x)//(fact(y))
    result=result//fact(x-y)
    return result
   
    
testcases=int(input())

for i in range(testcases):
    tables,people=input().split(" ")
    tables=int(tables)
    people=int(people)
    
    
    initial=people//tables
    extra=people%tables
        
    PA=initial+1
    PB=initial
    k=1
    for i in range(0,extra):
        k=k*ncr(people,PA)
        people=people-PA
            
    for i in range(extra,tables):
        k=k*ncr(people,PB)
        people=people-PB
            
    print(k)
        
            
