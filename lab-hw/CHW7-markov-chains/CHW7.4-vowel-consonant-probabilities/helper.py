import numpy as np
import numpy.linalg as la

def power_iteration(M, x):
    norm_tol = 1e-3
    stop_tol = 1e-7

    norm = la.norm(x, 1)
    if abs(norm - 1) > norm_tol:
        return x
        #raise Exception(f'x is not normalized! entry sum: {norm}')

    xc = M@x
    while la.norm(xc - x, 1) > stop_tol:
        x = xc
        xc = M@xc
    return xc
    
def isVowel(x):
    
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or 
        x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U' ):
        return True
    else:
        return False