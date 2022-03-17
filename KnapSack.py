# KnapSack using Recursion....

def KnapSack(EW,val,BC,n):
    if n == 0 or BC == 0:
        return 0
    
    if (EW[n-1] <= BC):
        return max( val[n-1] + KnapSack(EW,val,BC-EW[n-1],n-1),KnapSack(EW,val,BC,n-1) )
        
        
    else:
        return KnapSack(EW,val,BC,n-1)
        
        
        
weight = []
profit = []
num = int(input())
bagweight = int(input())

for i in range(num):
    x = int(input('weight'))
    y = int(input('profit'))
    weight.append(x)
    profit.append(y)

a = weight
b = profit

print(KnapSack(a,b,bagweight,num))



