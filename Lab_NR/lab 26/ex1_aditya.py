a = [[1,2,3],
     [2,3,4]]

b = [[3,4],
     [4,2],
     [5,8]]

def matrix_multiplication():
    a = []
    b = []
    a_row1 = list(map(int,input("Enter numbers for matrix row 1 for Matrix A, followed by ',': ")))
    a_row2 = list(map(int,input("Enter numbers for matrix row 2 for Matrix A, followed by ',': ")))
    b_row1 = list(map(int,input("Enter numbers for matrix row 1 for Matrix B, followed by ',': ")))
    b_row2 = list(map(int,input("Enter numbers for matrix row 2 for Matrix B, followed by ',': ")))
    b_row3 = list(map(int,input("Enter numbers for matrix row 3 for Matrix B, followed by ',': ")))

    a = a[a_row1, a_row2]
    b = b[b_row1, b_row2, b_row3]

    c = [[0 for columns in range(len(a))] for rows in range(len(b[0]))]
    # print(len(a[0]), len(b))
    if len(a[0]) == len(b):
        print("Error")
        return

    try:
        for rows in range(len(a)):
            for columns in range(len(b[0])):
                for rows_b in range(len(b)):
                    c[rows][columns] += a[rows][rows_b]*b[rows_b][columns]
        print(c)
    except IndexError as IE:
        print("Bad response, Index error: ", IE)
    except ValueError:
        print(ValueError)

matrix_multiplication()

