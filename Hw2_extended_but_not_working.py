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
    temp = []
    for i in range(len(lines)):
        temp.append(lines[i].split("\n")[0])
    alfa = float(temp[0])
    N = int(temp[1])

except Exception as e:
    print("\nInput file is defined incorrectly. Please enter a new input values.\n")
    with open("output_NewNM.txt", "a") as output_New:
        output_New.write("Input file is defined incorrectly. Please enter a new input values.\n")
    raise

def gauss(alfa, N):

    lower_d = []
    d = []
    upper_d = []

    for i in range(0,N-2):
        b = -alfa
        a = 1
        lower_d.append(b)
        d.append(1)


    upper_d = [0]*(N-1)
    upper_d[N-2] = 0

    for i in range(0, N - 3):
        b = alfa - 1
        upper_d.append(b)
    print(upper_d)

    b = []
    b.append(alfa)
    for i in range(1,N-2):
        b.append(0)


    for i in range(1,N-2):
        d[i] = d[i]-lower_d[i]/d[i-1]*upper_d[i-1]
        b[i] = b[i]- lower_d[i]/d[i-1]*b[i-1]


 # acayip kafam karıştı sondan başlayarak gidicem back subs yapıyorum
    x = [0] * N-1
    print(x)
    for i in reversed(range(len(x))):
        if i == N-2:
            x[i] = (b[i]) / d[i]
        else:
            x[i] = (b[i]-upper_d[i]*x[i+1])/d[i]

    return x


def jacobi(alfa, N):

    lower_d = []
    d = []

    for i in range(0, N - 2):
        b = -alfa
        a = 1
        lower_d.append(b)
        d.append(1)


    upper_d = [0] * (N - 1)
    upper_d[N - 2] = 0

    for i in range(0, N - 3):
        b = alfa - 1
        upper_d.append(b)


    b = []
    b.append(alfa)
    for i in range(1, N - 2):
        b.append(0)



    for i in range(0,3):
        if i == 0:
            x_o = [0] * (N - 1)
        else:
            x_o = x_n
        for i in range(0, N - 2):
            x_n = []
            x_n[i] = upper_d[i] * x_o[i + 1] + lower_d[i] * x_o[i - 1]

    return x_n


def siedel(alfa, N):

    lower_d = []
    d = []

    for i in range(0, N - 2):
        b = -alfa
        a = 1
        lower_d.append(b)
        d.append(1)


    upper_d = [0] * (N - 1)
    upper_d[N - 2] = 0

    for i in range(0, N - 3):
        b = alfa - 1
        upper_d.append(b)


    b = []
    b.append(alfa)
    for i in range(1, N - 2):
        b.append(0)



    for i in range(0,3):
        for i in range(0, N - 2):
            x_n = [0] * (N - 1)
            x_n[i] = upper_d[i] * x_n[i + 1] + lower_d[i] * x_n[i - 1]

    return x_n



x = gauss(float(alfa),float(N))

for i in range(0,N-2):
    print(x[i])


