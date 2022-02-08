def f(x):
    try:
        #f_function = (3**x) - 30
        #f_function = (1/x) - 30
        #f_function = math.sin(math.degrees(x)) - 0.1
        f_function = -(x**2) + 4
    
    except:
        print("f funciton is not defined properly. Please enter a correct function.")
        raise

    return f_function

