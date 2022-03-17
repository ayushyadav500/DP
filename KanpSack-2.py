# KanpSack using Top-Down approach....

def KnapSack(EW,val,BC,n):
    k = [[0 for i  in range(BC+1)]for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(BC+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif EW[i-1] <= BC:
                k[i][j] = max( val[i-1]+ k[i-1][j-EW[i-1]],k[i-1][j])
            else :
                k[i][j] = k[i-1][j]
                
    return k[n][BC]

weight = []
profit = []
num = int(input('number'))
bagweight = int(input('capacity'))

for i in range(num):
    x = int(input('weight'))
    y = int(input('profit'))
    weight.append(x)
    profit.append(y)

a = weight
b = profit

print(KnapSack(a,b,bagweight,num))
