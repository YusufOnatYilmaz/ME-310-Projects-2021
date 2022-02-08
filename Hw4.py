try:
    from f import f
    import matplotlib.pyplot as plt

except:
    print("\n")
    print("f.py is not in the correct location.")
    print("\n")
    raise

try:
    # Reading the input file
    with open('input.txt') as fi:
        lines = fi.readlines()

    input = []
    for line in lines:
        line = line.split("\n")[0]
        input.append(line)

    # Assigning values from the input file.
    number_of_equations = int(input[0])
    number_of_corrector_step = int(input[1])
    initial_independent_var = float(input[2])
    final_independent_var = float(input[3])
    step_size = float(input[4])
    initial_conditions = input[5].split(" ")

    # If there is a space at the end of the last line, code crushes. Because of the split function used above.
    # Below if statement solves this problem by simply deleting that element if it exists.
    if initial_conditions[-1] == "":
        del initial_conditions[-1]


    for i in range(len(initial_conditions)):
        initial_conditions[i] = float(initial_conditions[i])

except:
    print("\n")
    print("Error Defining the input file.")
    print("\n")
    raise

# Creating the x values according to the step size
x_values = []
for x in range(int((final_independent_var-initial_independent_var)/step_size) +1 ):
    x_values.append(initial_independent_var+step_size*x)


try:
    # Heun method
    def heun():
        
        y_values_for_heun = [initial_conditions,]

        for x in range(len(x_values)-1):

            y_values_for_step = [] # refreshing after each step-size
            
            # This file is parameterized by the number of equations given. However f.py file is not. 
            # When  number of equation changes, one should add it to the f.py file
            for ode in range(number_of_equations):
                
                # Below code block operates the heun method and correct the steps for number of corrector steps given in the input file.
                y_temp = y_values_for_heun[-1][ode] + f(x_values[x] ,y_values_for_heun[-1][ode], ode) * step_size

                for step in range(number_of_corrector_step): # corrector steps
                    y_temp = y_values_for_heun[-1][ode] + (f(x_values[x], y_values_for_heun[-1][ode], ode) + f(x_values[x+1], y_temp, ode))/2 * step_size

                y_values_for_step.append(y_temp)

            # Creating an array which contains results of all odes in the form of (number_of_y x number_of_ode) sized matrix
            y_values_for_heun.append(y_values_for_step)
        
        return y_values_for_heun

except:
    print("\n")
    print("Input values given are not consistent.")
    print("\n")
    raise

try:
    # Runge-Kutta method
    def runge_kutta():
        
        h = step_size
        y_values_for_rk = [initial_conditions,]

        for x in range(len(x_values)-1):
            
            y_values_for_step = [] # refreshing after each step-size

            for ode in range(number_of_equations): # Solves the 4th order runge-kutta method for each ode. 
                
                # Below equations are from the lecture notes.
                k1 = h * f(x_values[x], y_values_for_rk[-1][ode], ode)
                k2 = h * f(x_values[x] + h/2, y_values_for_rk[-1][ode] + k1/2, ode)
                k3 = h * f(x_values[x] + h/2, y_values_for_rk[-1][ode] + k2/2, ode)
                k4 = h * f(x_values[x] + h, y_values_for_rk[-1][ode] + k3, ode)

                y_values_for_step.append(y_values_for_rk[-1][ode] + (k1 + 2*k2 + 2*k3 + k4)/6)

            # Creating an array which contains results of all odes in the form of (number_of_y x number_of_ode) sized matrix    
            y_values_for_rk.append(y_values_for_step) 

        return y_values_for_rk

except:
    print("\n")
    print("Input values given are not consistent.")
    print("\n")
    raise

try:
    # Calling the functions
    y_values_for_heun = heun()
    y_values_for_rk = runge_kutta()

except:
    print("\n")
    print("Input values given are not consistent.")
    print("\n")
    raise


try:
    ## Writing the output file for Heun Method
    with open("output1.txt", "w") as output:

        # Below code segment is for writing the x and y to the top. It is parameterized by the number of equations.
        output.write("x_1     \t")
        for i in range(number_of_equations):
            output.write(f"y_{i+1}     \t")
        output.write("\n")
        output.write("==========\t"*(number_of_equations+1))
        output.write("\n")

        # Below code segment is for writing the results under the corresponding column. 
        # It is parameterized by the number of column which is equal to number of equations.
        for i in range(len(y_values_for_heun)):
            output.write("%f\t" % (x_values[i]))
            for ode in range(number_of_equations):
                output.write("%f\t" % (y_values_for_heun[i][ode])) # tab after putting each element
            output.write("\n")


    ## Writing the output file for Runge-Kutta Method
    with open("output2.txt", "w") as output:

        # Below code segment is for writing the x and y to the top. It is parameterized by the number of equations.
        output.write("x_1     \t")
        for i in range(number_of_equations):
            output.write(f"y_{i+1}     \t")
        output.write("\n")
        output.write("==========\t"*(number_of_equations+1))
        output.write("\n")

        # Below code segment is for writing the results under the corresponding column. 
        # It is parameterized by the number of column which is equal to number of equations.
        for i in range(len(y_values_for_rk)):
            output.write("%f\t" % (x_values[i])) 
            for ode in range(number_of_equations):
                output.write("%f\t" % (y_values_for_rk[i][ode])) # tab after putting each element
            output.write("\n")

except:
    print("\n")
    print("Input values given are not consistent.")
    print("\n")
    raise


### Printing output to the Screen

# Printing the Heun Method in the given format. ODE number is parameterized.
print("HEUN METHOD")
print("x_1     \t", end= "")
for ode in range(number_of_equations):
    print(f"y_{ode+1}     \t", end= "")

print()
print("==========\t"*(number_of_equations+1))

for i in range(len(y_values_for_heun)):
    print("%f\t" % (x_values[i]), end="") 
    for ode in range(number_of_equations):
        print("%f\t" % (y_values_for_heun[i][ode]), end="") # tab after putting each element
    print()

print()

# Printing the Runge-Kutta Method in the given format. ODE number is parameterized.
print("RUNGE-KUTTA METHOD")
print("x_1     \t", end= "")
for ode in range(number_of_equations):
    print(f"y_{ode+1}     \t", end= "")

print()
print("==========\t"*(number_of_equations+1))

for i in range(len(y_values_for_rk)):
    print("%f\t" % (x_values[i]), end="") 
    for ode in range(number_of_equations):
        print("%f\t" % (y_values_for_rk[i][ode]), end="") # tab after putting each element
    print()



### Below parts are for plotting
# Plotting part is in comment because it would take great effort to parameterize the number of plots
# with respect to the number of equations. Below commented part is valid for 3 equations

'''
heun_1 = []
heun_2 = []
heun_3 = []
rk_1 = []
rk_2 = []
rk_3 = []

# Seperating the indivudial results from 'y_values_for_heun' and 'y_values_for_rk'

for i in range(len(x_values)):
    heun_1.append(y_values_for_heun[i][0])
    heun_2.append(y_values_for_heun[i][1])
    heun_3.append(y_values_for_heun[i][2])
    rk_1.append(y_values_for_rk[i][0])
    rk_2.append(y_values_for_rk[i][1])
    rk_3.append(y_values_for_rk[i][2])


# Plotting the heun and runge-kutta" methods on the same graph

plt.plot(x_values, heun_3, label="heun", color = "green")
plt.plot(x_values, rk_3, label= "runge-kutta", color = "red")
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.title("Plots for ODE 3")
plt.show() 
'''