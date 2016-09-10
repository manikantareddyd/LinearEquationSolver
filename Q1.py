
import numpy as np
import sys
from math import sqrt

from scale import *
from pivot import *
from cholesky import *
from LUCrout import *
from LUGuass import *
from guass import *

# Although numpy matrices are "by reference", all functions return them for
# easy composition and return values can be safely ignored



methodPrompt = """
1. Gauss elimination (GE; without pivoting)
2. GE (with pivoting)
3. GE (with scaling and pivoting)
4. LU decomposition by using GE (without pivoting)
5. LU decomposition by using GE (with pivoting)
6. LU decomposition by using Crout method (without pivoting)
7. Cholesky decomposition (for symmetric positive definite matrix)
"""

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
