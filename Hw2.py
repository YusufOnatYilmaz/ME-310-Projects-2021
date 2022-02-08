try: #catching importing errors
    from matplotlib import pyplot as plt
    from gauss_medium import Gauss

except:

    # Error handling
    print("\nError importing the file.\n")
    with open("output.txt", "w") as output:
        output.write("Error importing the file.\n")
        raise

try: #catching file handling errors

    # Reading the input file
    with open('input.txt') as fi:
        lines = fi.readlines()

    # Resetting the output file
    with open('output.txt', "w") as fi:
        fi.write("")

except:

    # Error handling
    print("\nNo such file is found in the directory.\n")
    with open("output", "a") as output:
        output.write("No such file is found in the directory.\n")
    raise


# Below try-except catches the errors which occurs while defining the inputs
try: 
    # Sorting the input and assinging them into required variables
    temp = []
    for i in range(len(lines)):
        temp.append(lines[i].split("\n")[0])
    alfa = float(temp[0])
    N = int(temp[1])
    print("alpha value: " + str(alfa))
    print("Number of points: " + str(N))


except:

    # Error handling
    print("\nInput file is defined incorrectly. Please enter a new input values.\n")
    with open("output_NewNM.txt", "a") as output_New:
        output_New.write("Input file is defined incorrectly. Please enter a new input values.\n")
    raise


# Below try-except catches input errors. When N value is too low or negative, plotting function gives an error
try:

    if(alfa<1 and alfa>0): # Checking correct alpha values

        probabilities = Gauss(alfa,N) # Calling the gauss function from another file
        probabilities = probabilities[::-1] # Obtained probabilities is reversed. This line reverses the list of probablities 

        # Writing the values to output file.
        for i in range(len(probabilities)):
            with open("output.txt", "a") as output:
                output.write("%d\t%f\n" % (i,probabilities[i]))

        # x_points is created for plotting
        x_points = []
        for i in range(N+1):
            x_points.append(i) 

        # Plotting
        plt.plot(x_points,probabilities,"r")
        plt.xlabel("x_points")
        plt.ylabel("Probability")
        plt.title("Probability vs Point")
        #plt.show()

    else: # Code finishes when alpha is not a suitable value. 
        print("Alpha value has to be between 0 and 1.")        
    
except:
    print("Wrong input value")
    raise