import numpy as np
import sys
inputfile = 'input.txt'
outfile = sys.stdout
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
    print("\nx\n", file = outfile)
    for x in ans:
        print(x,file=outfile)
    return ans