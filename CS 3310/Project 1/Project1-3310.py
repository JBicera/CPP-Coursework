import numpy as np
import time

def classicMatrix(A,B):
    size = len(A)
    #Initialize Empty 2D Array
    C = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j] #Compute values for C
    return C

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

def randMatrix(size):
    return np.random.rand(size, size)

def runClassicTest(matA,matB):
    runtimes = []
    m = 10
    for i in range(m):
        start_time = time.perf_counter()
        classicMatrix(matA,matB)
        end_time = time.perf_counter()
        runtimes.append(end_time - start_time)
    total = 0
    for value in runtimes:
        total += value
    average = (total - max(runtimes) - min(runtimes)) / (m-2)
    return average

def runDACTest(matA,matB):
    runtimes = []
    m = 10
    for i in range(m):
        start_time = time.perf_counter()
        divideAndConquerMatrix(matA,matB)
        end_time = time.perf_counter()
        runtimes.append(end_time - start_time)
    total = 0
    for value in runtimes:
        total += value
    average = (total - max(runtimes) - min(runtimes)) / (m-2)
    return average

def runStrassenTest(matA,matB):
    runtimes = []
    m = 10
    for i in range(m):
        start_time = time.perf_counter()
        strassenMatrix(matA,matB)
        end_time = time.perf_counter()
        runtimes.append(end_time - start_time)
    total = 0
    for value in runtimes:
        total += value
    average = (total - max(runtimes) - min(runtimes)) / (m-2)
    return average
    
def main():
    #Randomly generated Matrices for test
    mat2A = randMatrix(2)
    mat2B = randMatrix(2)
    mat4A = randMatrix(4)
    mat4B = randMatrix(4)
    mat8A = randMatrix(8)
    mat8B = randMatrix(8)
    mat16A = randMatrix(16)
    mat16B = randMatrix(16)
    mat32A = randMatrix(32)
    mat32B = randMatrix(32)
    mat64A = randMatrix(64)
    mat64B = randMatrix(64)
    mat128A = randMatrix(128)
    mat128B = randMatrix(128)
    mat256A = randMatrix(256)
    mat256B = randMatrix(256)
    mat512A = randMatrix(512)
    mat512B = randMatrix(512)

    #Classic Matrix Test
    classicRuntimes = []
    classicRuntimes.append(runClassicTest(mat2A,mat2B))
    classicRuntimes.append(runClassicTest(mat4A,mat4B))
    classicRuntimes.append(runClassicTest(mat8A,mat8A))
    classicRuntimes.append(runClassicTest(mat16A,mat16B))
    classicRuntimes.append(runClassicTest(mat32A,mat32B))
    classicRuntimes.append(runClassicTest(mat64A,mat64B))
    classicRuntimes.append(runClassicTest(mat128A,mat128B))
    classicRuntimes.append(runClassicTest(mat256A,mat256B))
    classicRuntimes.append(runClassicTest(mat512A,mat512B))
    print("Classic Runtimes:")
    i = 1
    for value in classicRuntimes:
        print("Matrix size:{}x{} | Runtime: {:.2f}s".format(2**i,2**i,value))
        i+=1
    
    #Divide and Conquer Test
    dacRuntimes = []
    dacRuntimes.append(runDACTest(mat2A,mat2B))
    dacRuntimes.append(runDACTest(mat4A,mat4B))
    dacRuntimes.append(runDACTest(mat8A,mat8B))
    dacRuntimes.append(runDACTest(mat16A,mat16B))
    dacRuntimes.append(runDACTest(mat32A,mat32B))
    dacRuntimes.append(runDACTest(mat64A,mat64B))
    dacRuntimes.append(runDACTest(mat128A,mat128B))
    dacRuntimes.append(runDACTest(mat256A,mat256B))
    dacRuntimes.append(runDACTest(mat512A,mat512B))
    print("Divide and Conquer Runtimes")
    i = 1
    for value in dacRuntimes:
        print("Matrix size:{}x{} | Runtime: {:.2f}s".format(2**i,2**i,value))
        i+=1

    #Strassen Test
    strassenRuntimes = []
    strassenRuntimes.append(runStrassenTest(mat2A,mat2B))
    strassenRuntimes.append(runStrassenTest(mat4A,mat4B))
    strassenRuntimes.append(runStrassenTest(mat8A,mat8B))
    strassenRuntimes.append(runStrassenTest(mat16A,mat16B))
    strassenRuntimes.append(runStrassenTest(mat32A,mat32B))
    strassenRuntimes.append(runStrassenTest(mat64A,mat64B))
    strassenRuntimes.append(runStrassenTest(mat128A,mat128B))
    strassenRuntimes.append(runStrassenTest(mat256A,mat256B))
    strassenRuntimes.append(runStrassenTest(mat512A,mat512B))
    print("Strassen Runtimes")
    i = 1
    for value in strassenRuntimes:
        print("Matrix size:{}x{} | Runtime: {:.2f}s".format(2**i,2**i,value))
        i+=1
    

main()