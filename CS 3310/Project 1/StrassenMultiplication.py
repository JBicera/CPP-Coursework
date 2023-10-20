def strassenMatrix(A,B):
    n = len(A)
    #Base case when submatrices reduced down to 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n//2

    #Divide each matrices A and B
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    #Compute the seven products
    P1 = strassenMatrix(A11, subMatrix(B12, B22))
    P2 = strassenMatrix(addMatrix(A11, A12), B22)
    P3 = strassenMatrix(addMatrix(A21, A22), B11)
    P4 = strassenMatrix(A22, subMatrix(B21, B11))
    P5 = strassenMatrix(addMatrix(A11, A22), addMatrix(B11, B22))
    P6 = strassenMatrix(subMatrix(A12, A22), addMatrix(B21, B22))
    P7 = strassenMatrix(subMatrix(A11, A21), addMatrix(B11, B12))

    #Declare empty 2D array
    C = [[0 for i in range(n)] for j in range(n)]

    #Compute the submatrices of C
    C11 = addMatrix(subMatrix(addMatrix(P5, P4), P2), P6)
    C12 = addMatrix(P1, P2)
    C21 = addMatrix(P3, P4)
    C22 = subMatrix(addMatrix(P5, P1), addMatrix(P3, P7))

    # Combine sub-matrices to form result
    for i, (c11, c12) in enumerate(zip(C11, C12)):
        C[i][:mid] = c11
        C[i][mid:] = c12
    for i, (c21, c22) in enumerate(zip(C21, C22)):
        C[i + mid][:mid] = c21
        C[i + mid][mid:] = c22

    return C

def addMatrix(A,B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subMatrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

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

    C = strassenMatrix(A,B)

    print("Strassen Matrix Multiplication")
    print("------------------------------")
    for row in C:
        print(row)


main()