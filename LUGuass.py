import numpy as np
import sys
inputfile = 'input.txt'
outfile = sys.stdout
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

    print("\ny", file = outfile)
    for x in y:
        print(x,file=outfile)

    print("\nx", file = outfile)
    for x in ans:
        print(x,file=outfile)
    print("\n",file=outfile)
    
    print("L : \n", str(L)[1:-1], file = outfile)
    print("\nU : \n", str(U)[1:-1], file = outfile)
    return (L, U)