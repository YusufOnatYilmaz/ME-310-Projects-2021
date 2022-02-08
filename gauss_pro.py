

with open("input.txt","r+") as f:
    probability = float(f.readline())
    N = int(f.readline())

P = [1]
coefs = [probability]

#use N-index
coef_finder = lambda : probability/(1- coefs[-1] + coefs[-1] * probability)

iteration = 0


def factorial(index):
    factor = 1
    if(index ==1 ):
        return coefs[N-2]
    else:
        for i in range(1,index+1):
            factor = factor* coefs[N-i-1]
    return factor

#find coefficients backward propagation
for index in range(1,N-1):
    new_coefficient = coef_finder()
    coefs.append(new_coefficient)
    iteration +=1
    
#print("1.turn")
#print(iteration)
    
#find P values 
P.append(factorial(1))

for a in range(2,N):
    P.append(P[-1]*coefs[-a])
    iteration +=1

#print("2.turn")
#print(iteration)


P.append(0)
print(P)
# N == 5 => 6 iterations  N==10 => 16 iterations
#print("total")
print(iteration)


