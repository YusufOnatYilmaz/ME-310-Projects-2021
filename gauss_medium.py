
def Gauss(alfa, N): # Getting the alfa and N values

    # Creating the variables
    # Final lenghts of the lists will be as following:
    # lower_d and upper_d has the lenght N-2 
    # d, b has the lenght N-1
    # P has the lenght N+1
    # In order to finalize the lists with correct lenghts, required initial values are given in the variable decleration step. 
    lower_d = []
    d = [1]
    upper_d = []
    b = [alfa]
    P = [0]
    float_operation = 0

    # Filling the lists
    for i in range(0,N-2):

        second_prob = alfa - 1
        lower_d.append(-alfa)
        upper_d.append(second_prob)
        d.append(1)
        b.append(0)

    # Forward Elimination
    for i in range(1,N-1):

        # Value of in the diagonal is obtained after the following row operation  
        d[i] = d[i] - lower_d[i-1] / d[i-1] * upper_d[i-1] # In handwritten solution, lower_d must be taken as lower_d[i] as 'i' indicates the row number. 
        # In the code however, unless lower_d[i-1] is set, it results with the indexing error.   
        
        # Floating point operation counter
        float_operation +=1 

        # Value of in the B vector is obtained after the following row operation  
        b[i] = b[i] - lower_d[i-1] / d[i-1] * b[i-1]# In handwritten solution, lower_d must be taken as lower_d[i] as 'i' indicates the row number. 
        # In the code however, unless lower_d[i-1] is set, it results with the indexing error. 

        # Floating point operation counter
        float_operation +=1

    # Back Substitution
    for i in reversed(range(N-1)): # for loop is running from i=N-1 to i=0. Because back substition operation starts from the last row. 

        # Excluding the special case of N-2.
        if (i == N-2):
            P.append(b[i] / d[i])
            float_operation +=1

        # Calculating the probability values and adding them to a list for plotting.
        else:
            P.append((b[i]-upper_d[i] * P[-1]) / d[i])
            float_operation +=1
    
    print("Number of floating point operations: " + str(float_operation))

    # Appending the final probability value to the probability list
    P.append(1)

    return P