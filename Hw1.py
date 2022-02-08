try:
    import f
    import df
    from matplotlib import pyplot as plt
except:
    print("\nError importing the file.\n")
    with open("output_NewNM.txt", "a") as output_New:
        output_New.write("Error importing the file.\n")
        raise

# Function defined for matrix multiplication. This function took A and b as arguments and multiply them.
# A short method for this was numpy.matmul(A,b)
def multiply(A,b):
    temp_c = []
    for i in range(0, len(A)):
        temp=[]
        for j in range(0, len(b[0])):
            s = 0
            for k in range(0, len(A[0])):
                s += A[i][k] * b[k][j]
            temp.append(s)
        temp_c.append(temp)
    return temp_c

# Function defined for inverse matrix. This part was hard coded because 3x3 matrix solver was sufficient. Changing lenght of the matrix would be unnecesserly complex for this problem.
# A short method for this was numpy.linalg.inv(A)
def inverse_3X3_matrix(A_Matrix):

    determinant = A_Matrix[0][0] * ((A_Matrix[1][1] * A_Matrix[2][2]) - (A_Matrix[1][2] * A_Matrix[2][1])) - \
           A_Matrix[0][1] * ((A_Matrix[1][0] * A_Matrix[2][2]) - (A_Matrix[1][2] * A_Matrix[2][0])) + \
           A_Matrix[0][2] * ((A_Matrix[1][0] * A_Matrix[2][1]) - (A_Matrix[1][1] * A_Matrix[2][0]))

    coeff_1 = [(A_Matrix[1][1] * A_Matrix[2][2]) - (A_Matrix[1][2] * A_Matrix[2][1]),
                 -((A_Matrix[1][0] * A_Matrix[2][2]) - (A_Matrix[1][2] * A_Matrix[2][0])),
                 (A_Matrix[1][0] * A_Matrix[2][1]) - (A_Matrix[1][1] * A_Matrix[2][0])]

    coeff_2 = [-((A_Matrix[0][1] * A_Matrix[2][2]) - (A_Matrix[0][2] * A_Matrix[2][1])),
                 (A_Matrix[0][0] * A_Matrix[2][2]) - (A_Matrix[0][2] * A_Matrix[2][0]),
                 -((A_Matrix[0][0] * A_Matrix[2][1]) - (A_Matrix[0][1] * A_Matrix[2][0]))]

    coeff_3 = [(A_Matrix[0][1] * A_Matrix[1][2]) - (A_Matrix[0][2] * A_Matrix[1][1]),
                 -((A_Matrix[0][0] * A_Matrix[1][2]) - (A_Matrix[0][2] * A_Matrix[1][0])),
                 (A_Matrix[0][0] * A_Matrix[1][1]) - (A_Matrix[0][1] * A_Matrix[1][0])]
    
    try:
        inverse = [[1 / determinant * (coeff_1[0]), 1 / determinant * (coeff_2[0]), 1 / determinant * (coeff_3[0])],
                    [1 / determinant * (coeff_1[1]), 1 / determinant * (coeff_2[1]), 1 / determinant * (coeff_3[1])],
                    [1 / determinant * (coeff_1[2]), 1 / determinant * (coeff_2[2]), 1 / determinant * (coeff_3[2])]]
    except:
        print("\nDivision by zero leads to error. Please enter different input values.\n")
        with open("output_NewNM.txt", "a") as output_New:
            output_New.write("Division by zero leads to error. Please enter different input values.\n")
        raise

    return inverse

# Function defined for relative approximate error
def error_approximate(x_2, x_1):
    eps_a = (x_2 - x_1) / x_2
    return eps_a

# Function defined for the derivative of the 2nd order polynomial
def poly_derivative(a_1,a_2,x):
    value = a_1 + x*2*a_2
    return value

# Function defined for our algorithm to find the root of the nonlinear function
def ruya_onat_metot(x_1, x_2, x_3, i):

    try:
    # Matrix solving operations
        A = [[1, x_1, x_1**2], [1, x_3, x_3**2], [1, x_2, x_2**2]]
        b = [[f.f(x_1)], [f.f(x_3)], [f.f(x_2)]]
        A = inverse_3X3_matrix(A)
        C = multiply(A, b)
    
    except:
        print("\nSingular matrix occured. Please change the inputs or the functions\n")
        with open("output_NewNM.txt", "a") as output_New:
            output_New.write("Singular matrix occured. Please change the inputs or the functions\n")
        raise

    #Assigning the new values of a_0, a_1, a_2 
    a_0 = C[0][0]
    a_1 = C[1][0]
    a_2 = C[2][0]

    x_n = x_2 - ((f.f(x_2)) / poly_derivative(a_1, a_2, x_2)) # New root estimation

    eps_a = error_approximate(x_2, x_3)

    print("%d\t\t%.8f\t\t%.8f\t\t%.8f\t%.8f\n" % (i, x_n, x_1, x_3, eps_a))
    print("Number of functions: " + str(5*i) + "\n")

    # Writing the output file for Ruya-Onat method
    output_data = "%d\t\t%.8f\t\t%.8f\t\t%.8f\n" % (i+1, x_n, f.f(x_n), eps_a*100)
    if i == 0:
        output_data = "%d\t\t%.8f\t\t%.8f\t\t%s\n" % (i+1, x_n, f.f(x_n), "undefined")
    with open("output_NewNM.txt", "a") as output_New:
        output_New.write(output_data)

    # Returing the results of Ruya-Onat method
    return [x_3, x_n, x_2, i+1, eps_a]

# Function defined for the Newton-Raphson method
def Newton_Raphson(x_2, i):
    x_1 = x_2

    try:
        x_2 = x_2 - f.f(x_2)/df.df(x_2)
    
    except:
        print("\nDivision by zero leads to error. Please enter different input values.\n")
        with open("output_NM.txt", "a") as output_NM:
            output_NM.write("Division by zero leads to error. Please enter different input values.\n")
        raise

    eps_a = error_approximate(x_2, x_1)

    print("%d\t\t%.8f\t\t%.8f\n" % (i, x_2, eps_a))
    print("Number of functions: " + str(2*i) + "\n")

    # Writing the output file for the Newton-*Raphson method
    output_data = "%d\t\t%.8f\t\t%.8f\t\t%.8f\n" % (i+1, x_2, f.f(x_2), eps_a*100)
    if i == 0:
        output_data = "%d\t\t%.8f\t\t%.8f\t\t%s\n" % (i+1, x_2, f.f(x_2), "undefined")    
    with open("output_NM.txt", "a") as output_NM:
        output_NM.write(output_data)

    # Returing the results of Newton-Raphson method
    return [x_2, i+1, eps_a]

# Function defined for the Secant method
def Secant(x_1,x_2, i, fx_1, fx_2):

    try:
        x_3 = x_1- fx_1*(x_2-x_1)/(fx_2-fx_1)
    
    except:
        print("\nDivision by zero leads to error. Please enter different input values.\n")
        with open("output_SM.txt", "a") as output_SM:
            output_SM.write("Division by zero leads to error. Please enter different input values.\n") 
        raise
    
    eps_a = error_approximate(x_2, x_3)

    # Assinging the necessary values to necessary variables
    x_1 = x_2
    fx_1 = fx_2
    x_2 = x_3
    fx_2 = f.f(x_2)

    print("%d\t\t%.8f\t\t%.8f\n" % (i, x_2, eps_a))
    print("Number of functions: " + str(i) + "\n") # Only one function is called in this method as old values are obtained from a list. 

    # Writing the output file for the Secant Method
    output_data = "%d\t\t%.8f\t\t%.8f\t\t%.8f\n" % (i+1, x_2, f.f(x_2), eps_a*100)
    if i == 0:
        output_data = "%d\t\t%.8f\t\t%.8f\t\t%s\n" % (i+1, x_2, f.f(x_2), "undefined")
    with open("output_SM.txt", "a") as output_SM:
        output_SM.write(output_data) 

    # Returing the results of Secant method
    return [x_1, x_2, i+1, fx_1, fx_2, eps_a]


try:
    # Reading the input file
    with open('input.txt') as fi:
        lines = fi.readlines()
except:
    print("\nNo such file is found in the directory.\n")
    with open("output_NewNM.txt", "a") as output_New:
        output_New.write("No such file is found in the directory.\n")
    raise

try:
    # Sorting the input into required variables
    temp =[]
    for i in range(len(lines)):
        temp.append(lines[i].split("\n")[0]) 
    x_1 = float(temp[0])
    x_2 = float(temp[1])
    x_3 = (x_1+x_2) / 2
    E_s = float(temp[2])
    i_max = int(temp[3])


except Exception as e:
    print("\nInput file is defined incorrectly. Please enter a new input values.\n")
    with open("output_NewNM.txt", "a") as output_New:
        output_New.write("Input file is defined incorrectly. Please enter a new input values.\n")
    raise 

i = 0
place_holder = 1

# Preparing the lists for data storage. Datas will come from methods and will send to methods from these lists.
ruya_onat_value = [[x_1, x_2, x_3, i, place_holder]]
newton_value = [[x_1, i, place_holder]]
secant_value = [[x_1, x_2, i, f.f(x_1), f.f(x_2), place_holder]]


# Above variables will trace the index for plotting. Lists above will have a lenght of the iteration number of the corresponding methods and their lenght might vary. 
k = 0
j = 0
l = 0

# deleting the inside of the output files for every run
with open("output_NewNM.txt", "w") as output_New:
    output_New.write("")

# Below for loops gets the returing values from the methods and store them in a list. In the same line last values are also send to the next iteration. This loops also checks whether it is time to stop the iterations.
for i in range(i_max):
    ruya_onat_value.append(ruya_onat_metot(ruya_onat_value[i][0], ruya_onat_value[i][1], ruya_onat_value[i][2], ruya_onat_value[i][3]))
    k = i 
    if abs(ruya_onat_value[i+1][4]) < E_s:
        break

# Deleting the inside of the output files for every run
with open("output_NM.txt", "w") as output_New:
    output_New.write("")

# Below for loops gets the returing values from the methods and store them in a list. In the same line last values are also send to the next iteration. This loops also checks whether it is time to stop the iterations.
for i in range(i_max):
    newton_value.append(Newton_Raphson(newton_value[i][0], newton_value[i][1]))
    j = i
    if abs(newton_value[i+1][2]) < E_s:
        break

# Deleting the inside of the output files for every run
with open("output_SM.txt", "w") as output_New:
    output_New.write("")

# Below for loops gets the returing values from the methods and store them in a list. In the same line last values are also send to the next iteration. This loops also checks whether it is time to stop the iterations.
for i in range(i_max):
    secant_value.append(Secant(secant_value[i][0], secant_value[i][1], secant_value[i][2], secant_value[i][3], secant_value[i][4]))
    l = i
    if abs(secant_value[i+1][5]) < E_s:
        break

# Preparing lists for plots
error_for_ruya_onat = []
root_estimate_for_ruya_onat = []
error_for_newton = []
root_estimate_for_newton = []
error_for_secant = []
root_estimate_for_secant = []

# Below for loops adjust the lists of error and root estimate values. Lists are adjusted such that all values can be seen in the same plot.
for i in range(k):
    error_for_ruya_onat.append(abs(ruya_onat_value[i][4])*100) # multiply with 100 for percentage error 
    root_estimate_for_ruya_onat.append(ruya_onat_value[i][1]) #

for i in range(i_max-k):
    error_for_ruya_onat.append(0)
    root_estimate_for_ruya_onat.append(root_estimate_for_ruya_onat[k-1])

for i in range(j):
    error_for_newton.append(abs(newton_value[i][2])*100) # multiply with 100 for percentage error 
    root_estimate_for_newton.append(newton_value[i][0])

for i in range(i_max-j):
    error_for_newton.append(0)
    root_estimate_for_newton.append(root_estimate_for_newton[j-1]) # multiply with 100 for percentage error 

for i in range(l):
    error_for_secant.append(abs(secant_value[i][5])*100)
    root_estimate_for_secant.append(secant_value[i][1])

for i in range(i_max-l):
    error_for_secant.append(0)
    root_estimate_for_secant.append(root_estimate_for_secant[l-1])

x_axis = []
for i in range(1,i_max):
    x_axis.append(i)

#deleting the first index as it is undefined
del error_for_ruya_onat[0]
del error_for_newton[0]
del error_for_secant[0]
del root_estimate_for_ruya_onat[0]
del root_estimate_for_newton[0]
del root_estimate_for_secant[0]

# Plots a=1 shows the error graphs and a=0 shows the root estimate plots
# It is highly recommended to examine the plots in the fullscreen. By default it is set to a small size but it is prepared for a bigger size.

a = 0

if a:

    figure, axis = plt.subplots(2, 2)

    axis[0, 0].plot(x_axis, error_for_ruya_onat)
    axis[0, 0].set_title("Ruya-Onat Method (Error vs Iteration Number)")

    axis[0, 1].plot(x_axis, error_for_newton)
    axis[0, 1].set_title("Newton-Raphson Method (Error vs Iteration Number)")

    axis[1, 0].plot(x_axis, error_for_secant)
    axis[1, 0].set_title("Secant Method (Error vs Iteration Number)")

    plt.plot(x_axis, error_for_ruya_onat)
    plt.plot(x_axis, error_for_newton)
    plt.plot(x_axis, error_for_secant)
    plt.title("Error vs Iteration Number (for all Methods)")
    plt.xlabel("Iteration number")
    plt.ylabel("Relative Percent Error")
    plt.legend(["Ruya-Onat", "Newton-Raphson", "Secant"])
    plt.show()

else:

    figure, axis = plt.subplots(2, 2)

    axis[0, 0].plot(x_axis, root_estimate_for_ruya_onat)
    axis[0, 0].set_title("Ruya-Onat Method (Root Estimate vs Iteration Number)")

    axis[0, 1].plot(x_axis, root_estimate_for_newton)
    axis[0, 1].set_title("Newton-Raphson Method (Root Estimate vs Iteration Number)")

    axis[1, 0].plot(x_axis, root_estimate_for_secant)
    axis[1, 0].set_title("Secant Method (Root Estimate vs Iteration Number)")

    plt.plot(x_axis, root_estimate_for_ruya_onat, "r")
    plt.plot(x_axis, root_estimate_for_newton, "g")
    plt.plot(x_axis, root_estimate_for_secant)
    plt.title("Root Estimation vs Iteration Number")
    plt.xlabel("Iteration number")
    plt.ylabel("Root Estimation ")
    plt.legend(["Ruya-Onat", "Newton-Raphson", "Secant"])
    plt.show()
