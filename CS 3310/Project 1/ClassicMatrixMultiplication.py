def classicMatrix(A,B):
    size = len(A)
    #Initialize Empty 2D Array
    C = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j] #Compute values for C
    return C

def main():
    #Insert example Matrices to run here
    A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

    B = [[16, 15, 14, 13],
     [12, 10, 11, 9],
     [8, 7, 6, 5],
     [4, 3, 2, 1]]

    C = classicMatrix(A,B)
    print("Classic Matrix Multiplication")
    print("-----------------------------")
    for row in C:
        print(row)


main()