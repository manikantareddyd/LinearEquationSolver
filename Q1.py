import numpy as np
import sys
from math import sqrt
# Although numpy matrices are "by reference", all functions return them for
# easy composition and return values can be safely ignored

inputfile = 'input.txt'
outfile = sys.stdout



methodPrompt = """
1. Gauss elimination (GE; without pivoting)
2. GE (with pivoting)
3. GE (with scaling and pivoting)
4. LU decomposition by using GE (without pivoting)
5. LU decomposition by using GE (with pivoting)
6. LU decomposition by using Crout method (without pivoting)
7. Cholesky decomposition (for symmetric positive definite matrix)
"""

def scale(mat, baseval = 1.) :
    nrows, ncols = mat.shape
    for i in range(0,nrows) :
        maxindex = np.argmax(mat[i,:])
        mat[i] = mat[i]/mat[i,maxindex]
    return mat


def pivot(mat) :
    nrows, ncols = mat.shape
    for i in range(0,nrows) :
        maxindex = np.argmax(mat[i:,i]) + i
        mat[[maxindex, i]] = mat[[i, maxindex]]
    print("Permutation Matrix : \n", str(mat)[1:-1], file = outfile)
    return mat

def gaussElimination(mat) :
    nrows, ncols = mat.shape
    ans = [0]*(nrows)
    for i in range(0,nrows) :
        for j in range(i+1, nrows) :
            mat[j] = mat[j] - mat[i]*(mat[j,i]/mat[i,i])
    for i in range(nrows-1,-1,-1) :
        temp = mat[i,nrows]
        for j in range(i, nrows) :
            temp -= ans[j]*mat[i,j]
        ans[i] = temp/mat[i,i]
    print("\nSolution is : ", ans, file = outfile)
    return ans

def LUusingGaussElimination(mat) :
    nrows, ncols = mat.shape
    U = np.copy(mat[:,:-1])
    L = np.identity(nrows)
    ans = [0]*(nrows)
    y = [0]*(nrows)
    for i in range(0,nrows) :
        for j in range(i+1, nrows) :
            temp = U[j,i]/U[i,i]
            U[j] = U[j] - U[i]*(temp)
            L[j,i] = temp

    for i in range(0,nrows) :
        temp = mat[i,nrows]
        for j in range(0, i) :
            temp -= y[j]*L[i,j]
        y[i] = temp/L[i,i]

    for i in range(nrows-1,-1,-1) :
        temp = y[i]
        for j in range(i, nrows) :
            temp -= ans[j]*U[i,j]
        ans[i] = temp/U[i,i]

    print("Intermediate(y) is : ", y, file = outfile)
    print("Solution is : ", ans, file = outfile)
    print("L : \n", str(L)[1:-1], file = outfile)
    print("U : \n", str(U)[1:-1], file = outfile)
    return (L, U)

def LUusingCrout(mat) :
    nrows, ncols = mat.shape
    back = np.copy(mat)
    mat = mat[:,:-1]
    U = np.matrix(np.identity(nrows))
    L = np.matrix(np.identity(nrows))
    for j in range(0,nrows) :
        L[j:,j] = mat[j:,j] - L[j:,:j]*U[:j,j]
        U[j,j+1:] = (mat[j,j+1:] - L[j,:j]*U[:j,j+1:])/L[j,j]
    mat = back
    ans = [0]*(nrows)
    y = [0]*(nrows)
    for i in range(0,nrows) :
        temp = mat[i,nrows]
        for j in range(0, i) :
            temp -= y[j]*L[i,j]
        y[i] = temp/L[i,i]

    for i in range(nrows-1,-1,-1) :
        temp = y[i]
        for j in range(i, nrows) :
            temp -= ans[j]*U[i,j]
        ans[i] = temp/U[i,i]

    print("Intermediate(y) is : ", y, file = outfile)
    print("Solution is : ", ans, file = outfile)
    print("L : \n", str(L)[1:-1], file = outfile)
    print("U : \n", str(U)[1:-1], file = outfile)
    return

def cholesky(mat) :
    nrows, ncols = mat.shape
    L = np.matrix(np.identity(nrows))
    for i in range(0,nrows):
        for j in range(0, i+1):
            s = sum(L[i,k] * L[j,k] for k in range(0,j))
            L[i,j] = sqrt(mat[i,i] - s) if (i == j) else \
                      (1.0 / L[j,j] * (mat[i,j] - s))
    U = L.transpose()
    ans = [0]*(nrows)
    y = [0]*(nrows)
    for i in range(0,nrows) :
        temp = mat[i,nrows]
        for j in range(0, i) :
            temp -= y[j]*L[i,j]
        y[i] = temp/L[i,i]

    for i in range(nrows-1,-1,-1) :
        temp = y[i]
        for j in range(i, nrows) :
            temp -= ans[j]*U[i,j]
        ans[i] = temp/U[i,i]
    print("Intermediate(y) is : ", y, file = outfile)
    print("Solution is : ", ans, file = outfile)
    print("L : \n", str(L)[1:-1], file = outfile)
    return

methodMap = {
    1 : gaussElimination,
    2 : (lambda x : gaussElimination(pivot(x))),
    3 : (lambda x : gaussElimination(pivot(scale(x)))),
    4 : LUusingGaussElimination,
    5 : (lambda x : LUusingGaussElimination(pivot(x))),
    6 : LUusingCrout,
    7 : cholesky
}

if __name__=="__main__" :
    with open(inputfile) as f:
        n = [int(x) for x in next(f).split()]
        mat = [[float(x) for x in line.split()] for line in f]
    mat = np.matrix(mat)
    print(methodPrompt)
    method = int(input())
    methodMap[method](mat)
