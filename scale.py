import numpy as np
import sys
inputfile = 'input.txt'
outfile = sys.stdout

def scale(mat, baseval = 1.) :
    nrows, ncols = mat.shape
    for i in range(0,nrows) :
        maxindex = np.argmax(mat[i,:])
        mat[i] = mat[i]/mat[i,maxindex]
    return mat