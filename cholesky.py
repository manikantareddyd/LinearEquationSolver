import numpy as np
import sys
from math import sqrt
inputfile = 'input.txt'
outfile = sys.stdout

def CholeskyLUDecomposition(mat) :
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
    
    print("\ny", file = outfile)
    for x in y:
        print(x,file=outfile)

    print("\nx", file = outfile)
    for x in ans:
        print(x,file=outfile)
    print("\n",file=outfile)

    print("L : \n", str(L)[1:-1], file = outfile)
    return