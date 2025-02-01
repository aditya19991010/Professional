'''List,tuple, dictionary and set'''


'''create a list of 2x2 matrix'''
''' 1. matrix addition
 2. count number of occurrences of an item in a list
 3. swap the 1st and last element of the list
'''

def matrix_add():
    for row in range(len(A)):
        for column in range(len(B[0])):
            C[row][column] = A[row][column] + B[row][column]

    for r in C:
        print(r)
    print("\n")

def matrix_multi():

    for row in range(len(A)):
        for column in range(len(B)):
            C[row][column] = A[row][column] * B[row][column]

    for r in C:
        print(r)


def main():
    matrix_add()
    matrix_multi()


if __name__ == "__main__":
    A = [[2, 4, 5], [4, 5, 6], [5, 6, 7]]
    B = [[4, 5, 6], [5, 6, 7], [2, 4, 5]]
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    main()