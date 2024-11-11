a = [[1,2,3],
     [2,3,4]]

b = [[3,4],
     [4,2],
     [5,8]]

def matrix_multiplication():
    print("Initiating Matrix multiplication of A(2x3) and B(3x2) matrix.\nEnter the number in format : 2,3,4 or 6,4\n")
    a = []
    b = []

    a_row1 = list(map(int,input("Enter numbers for matrix row 1 for Matrix A, followed by ',': ").split(",")))
    a_row2 = list(map(int,input("Enter numbers for matrix row 2 for Matrix A, followed by ',': ").split(",")))
    b_row1 = list(map(int,input("Enter numbers for matrix row 1 for Matrix B, followed by ',': ").split(",")))
    b_row2 = list(map(int,input("Enter numbers for matrix row 2 for Matrix B, followed by ',': ").split(",")))
    b_row3 = list(map(int,input("Enter numbers for matrix row 3 for Matrix B, followed by ',': ").split(",")))
    # print(a_row1, a_row2)
    a.append(a_row1)
    a.append(a_row2)

    b.append(b_row1)
    b.append(b_row2)
    b.append(b_row3)

    c = [[0 for columns in range(len(a))] for rows in range(len(b[0]))]
    # print(len(a[0]), len(b))
    if len(a[0]) != len(b):
        print("Error")
        return

    try:
        for rows in range(len(a)):
            for columns in range(len(b[0])):
                for rows_b in range(len(b)):
                    c[rows][columns] += a[rows][rows_b]*b[rows_b][columns]
        print(f"Matrix mutiplication of {a} and {b} is :\n ",c)
    except IndexError as IE:
        print("Bad response, Index error: ", IE)
    except ValueError:
        print(ValueError)

matrix_multiplication()

