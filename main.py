import numpy as np
import sys
from math import sqrt

from scale import *
from pivot import *
from cholesky import *
from LUCrout import *
from LUGuass import *
from guass import *

methods = """
1. Gauss elimination (GE; without pivoting)
2. GE (with pivoting)
3. GE (with scaling and pivoting)
4. LU decomposition by using GE (without pivoting)
5. LU decomposition by using GE (with pivoting)
6. LU decomposition by using Crout method (without pivoting)
7. LU Cholesky decomposition (for symmetric positive definite matrix)
"""

methodMap = {
    1 : GaussElimination,
    2 : (lambda x : GaussElimination(pivot(x))),
    3 : (lambda x : GaussElimination(pivot(scale(x)))),
    4 : GaussLUDecomposition,
    5 : (lambda x : GaussLUDecomposition(pivot(x))),
    6 : CroutLUDecomposition,
    7 : CholeskyLUDecomposition
}

methodNameMap = {
    1: "Gauss elimination (GE; without pivoting)",
    2: "GE (with pivoting)",
    3: "GE (with scaling and pivoting)",
    4: "LU decomposition by using GE (without pivoting)",
    5: "LU decomposition by using GE (with pivoting)",
    6: "LU decomposition by using Crout method (without pivoting)",
    7: "LU Cholesky decomposition (for symmetric positive definite matrix)" 
}

if __name__=="__main__" :
    with open(inputfile) as f:
        n = [int(x) for x in next(f).split()]
        mat = [[float(x) for x in line.split()] for line in f]
    mat = np.matrix(mat)
    for i in methodNameMap:
        print(i,":",methodNameMap[i])
    method = int(input())
    print(methodNameMap[method],file=outfile)
    methodMap[method](mat)
