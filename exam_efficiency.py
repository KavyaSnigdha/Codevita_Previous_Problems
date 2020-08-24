from decimal import *
import math
getcontext().prec = 11
def calculate(x, i, dif): 
    m = Decimal(dif+i*x)/Decimal(2*i)
    accu = Decimal(100*m)/Decimal(x)
    val = "{:.2f}".format(accu)
    if val[-3:] == ".00": 
        return val[:-3]
    return val

x1 = float(input())
x2 = float(input())
x3 = float(input())
y = float(input())
#case-1 for X1 minimum accuracy
val = x2*2+3*x3
if val >= y: 
    print("One mark question need not be attempted, so no minimum accuracy rate applicable")
else: 
    dif = y-val
    val = calculate(x1,1,dif)
    print("Minimum Accuracy rate required for One mark question is",val,end="%")
    print()
    
#case-2 for x2 minimum accuracy
val = x1*1+3*x3
if val >= y: 
    print("Two mark question need not be attempted, so no minimum accuracy rate applicable")
else: 
    dif = y-val
    val = calculate(x2,2,dif)
    print("Minimum Accuracy rate required for Two mark question is",val,end="%")
    print()
#case-3 for x2 minimum accuracy
val = x1*1+2*x2
if val >= y: 
    print("Three mark question need not be attempted, so no minimum accuracy rate applicable")
else: 
    dif = y-val
    val = calculate(x3,3,dif)
    print("Minimum Accuracy rate required for Three mark question is",val,end="%")
