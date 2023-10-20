
def divideAndConquerMatrix(A,B):
    n = len(A)
    #Base case when submatrices reduced down to 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        mid = n//2

        #Divide each matrix A and B into four submatrices
        A11 = [row[:mid] for row in A[:mid]]
        A12 = [row[mid:] for row in A[:mid]]
        A21 = [row[:mid] for row in A[mid:]]
        A22 = [row[mid:] for row in A[mid:]]

        B11 = [row[:mid] for row in B[:mid]]
        B12 = [row[mid:] for row in B[:mid]]
        B21 = [row[:mid] for row in B[mid:]]
        B22 = [row[mid:] for row in B[mid:]]

        #Compute the submatrices of C
        C11 = addMatrix(divideAndConquerMatrix(A11, B11),divideAndConquerMatrix(A12, B21))
        C12 = addMatrix(divideAndConquerMatrix(A11, B12),divideAndConquerMatrix(A12, B22))
        C21 = addMatrix(divideAndConquerMatrix(A21, B11),divideAndConquerMatrix(A22, B21))
        C22 = addMatrix(divideAndConquerMatrix(A21, B12),divideAndConquerMatrix(A22, B22))

        #Declare empty 2D array
        C = [[0 for i in range(n)] for j in range(n)]

        #Combine C submatrices by concatenating in right order
        for i, (c11, c12) in enumerate(zip(C11, C12)):
            C[i][:mid] = c11
            C[i][mid:] = c12
        for i, (c21, c22) in enumerate(zip(C21, C22)):
            C[i + mid][:mid] = c21
            C[i + mid][mid:] = c22

        return C
def addMatrix(A,B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def main():
    A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

    B = [[16, 15, 14, 13],
     [12, 10, 11, 9],
     [8, 7, 6, 5],
     [4, 3, 2, 1]]

    C = divideAndConquerMatrix(A, B)

    print("Divide and Conquer Matrix Multiplication")
    print("----------------------------------------")
    for row in C:
        print(row)
main()