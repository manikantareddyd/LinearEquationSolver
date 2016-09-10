import numpy as np
import sys
inputfile = 'input.txt'
outfile = sys.stdout
def pivot(mat) :
    nrows, ncols = mat.shape
    for i in range(0,nrows) :
        maxindex = np.argmax(mat[i:,i]) + i
        mat[[maxindex, i]] = mat[[i, maxindex]]
    print("\nPivotted Matrix : \n", str(mat)[1:-1], file = outfile)
    return mat