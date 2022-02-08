# If new ODEs added to the input file.
# New ones should be added like the below format

# parameterizing this section is solved by brute force.
# Otherwise is beyond my understanding in Python.

def f(x, y, ode_number=1):

    # number of zeros in the ode_array must be greater or equal to the number of equations.
    ode_array = [0,0,0,0]
    ode_array[0] = y
    ode_array[1] = x+y
    ode_array[2] = x*y
    ode_array[3] = x - 2*y*x

    return ode_array[ode_number]


    """
    # Below format also works but it is not preferred. It is bad practise.

    if ode_number == 0:
        f1 = -3*x + 3*y
        return f1

    elif ode_number == 1:
        f2 = x - 2*y
        return f2 

    elif ode_number == 2:
        f3 = -3*x - 2*y*x
        return f3

    elif ode_number == 3:
        f3 = -3*x - 2*y*x
        return f3

    elif ode_number == 4:
        f4 =  x - 2*y*x
        return f4
"""


