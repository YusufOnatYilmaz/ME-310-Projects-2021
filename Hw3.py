try:
    import matplotlib.pyplot as plt
    import numpy as np

except:
    # Error handling
    print("\nError importing the packages.\n")
    raise


try: 
    # Reading the input file
    with open('input.txt') as fi:
        lines = fi.readlines()

except:

    # Error handling
    print("\nNo such file is found in the directory.\n")
    raise

x = []
y= []

try:
    # Seperating the variables in the input file to x and y.
    for line in lines:
        temp = line.split(" ")  # Seperating x and y values
        temp2 = temp[1].split("\n") # Cleaning the y datas 
        del temp2[1]
        y.append(float(temp2[0])) # Creating the y input array
        x.append(float(temp[0])) # Creating the x input array

except:
    print("Given input file defined incorrectly.")
    print("Most common error is not giving an empty line as a last line.")

# Defining the n value in the project. N value is one less than the number of points.
N = len(x)-1

# Pre-defining the A and b matrices. np.zeros function is used in this step because 
# most of the values in these array are 0. With this approach only necessary one will be replaced. 
A = np.zeros((4*N,4*N))  
b = np.zeros((4*N))

# k and i values are defined for counting. k values are not necesserly compatible with 
# "k" value given in the project. "k" is just a counter.
i = 0
k = 0

# Below for loop creates the A matrix.
# There is pattern in every 4 line. These patterns come from the conditions of the cubic-spline system.
# This for loop iterates through lines and assign the necessary values to their correct places in the matrix.
# Below if statements seperates each line in the patterns.
# Important note here is that values other than the ones assigned in this step are 0.
for line in A:

    # Defining the x(i+1)-x(i) on every iteration. Defining it as hi allows a short cut for future usage.
    hi = x[k+1] - x[k]    

    if i%4 == 0: 
        # First lines in the pattern only consist of 1.
        # This equation comes from the first condition.
        # This equation is obtained by solving the S_k[x_i] function.
        line[i] = 1 
        i+=1

    elif i%4 == 1: 
        # Second lines in the pattern consist of powers of hi values.
        # This equation comes from the second condition.
        # This equation is obtained by solving the S_k[x_(i+1)] function.
        line[i] = hi
        line[i+1] = hi*hi
        line[i+2] = hi*hi*hi
        i+=1

    elif i%4 == 2:
        # Third lines in the pattern consist of powers of hi values.
        # This equation comes from the third condition.
        # This equation is obtained by solving the first derivative of S_k.
        line[i-1] = 1
        line[i] = 2*hi
        line[i+1] = 3*hi*hi

        # -1 cant be assign in the last pattern because it goes beyond the limits of the matrix. This problem is solved by the fifth condition.
        if i < 4*N-4:
            # For internal points, values of the first derivatives on left and right splines are equal to each other. 
            # -1 comes from that equation.
            line[i+3] = -1 
        i+=1
    
    elif i%4 == 3:
        # Forth lines in the pattern consist of powers of hi values.
        # This equation comes from the Forth condition.
        # This equation is obtained by solving the second derivative of S_k.
        line[i-1] = 2
        line[i] = 6*hi
        # -2 cant be assign in the last pattern because it goes beyond the limits of the matrix. This problem is solved by the fifth condition.
        if i < 4*N-4: 
            # For internal points, values of the second derivatives on left and right splines are equal to each other.
            # -2 comes from that equation.
            line[i+3] = -2 

        # Counting the i and k
        i+=1
        k+=1


# k and i values are again defined for counting.
i = 0
k = 0

# Below for loop creates the b matrix.
# There is pattern in every 4 line. These patterns come from the conditions of the cubic-spline system.
# This for loop iterates through lines and assign the necessary values to their correct places in the matrix.
# Below if statements seperates each line in the patterns.
for i in range(len(b)) :

    yi = y[k+1]-y[k] # This value will be used in the second step of the pattern.

    if i%4 == 0:
        # Corresponding results of the first condition.
        b[i] = y[k]
        i+=1

    elif i%4 == 1:
        # Corresponding results of the second condition.
        b[i] = yi
        i+=1

    elif i%4 == 2:
        # Corresponding results of the third condition.
        b[i] = 0
        i+=1
    
    elif i%4 == 3:
        # Corresponding results of the forth condition.
        b[i] = 0
        i+=1
        k+=1

try:
    # Inverse of the A matrix
    A = np.linalg.inv(A)

    # Matrix is the multiplication A^-1 and b matrixes.
    # Size of the obtained C matrix is 4Nx1.
    C  = np.matmul(A,b)

except:
    print("Determinant of A is 0 which gives no results.")
    print("Please define another input file.")
    raise

# This step turns the size of C matrix to Nx4.

D = [] # D is a replacement for C.
for i in range(N):
    
    e= [] # e is a dummy variable which is not used beyond the scope of this for loop.
    for k in range(4):
        e.append(C[k+i*4])
    D.append(e)


# Outputing "C" matrix to screen in the desired format.
print(D)


# Below this part is for plotting.
# numpy and matplotlib functions in this step are used only for plotting purposes. 
# They do not change the results.


# x and y values on the plot.
y_for_plot = []
x_for_plot = []

for i in range(N):

    # Plotting with only given x values would result in linear-like curves.
    # In order to smooth the curves, new x values between the given x values are defined.
    x_plot = np.arange(start=x[i], stop=x[i+1], step=0.1) # only for plotting
    

    for x_temp in x_plot:
        # Below line solves the S_k(x) function for every x values given. Obtained results will be shown in the plot.
        yi = D[i][0] + D[i][1]*(x_temp - x[i]) + D[i][2]*(x_temp - x[i])**2 + D[i][3]*(x_temp - x[i])**3
        y_for_plot.append(yi)
        x_for_plot.append(x_temp)

# plotting functions
plt.plot(x_for_plot, y_for_plot)
plt.xlabel('x')
plt.ylabel('y')
plt.title("x vs y")
plt.show()
