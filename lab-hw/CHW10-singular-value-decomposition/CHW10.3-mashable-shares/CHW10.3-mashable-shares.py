import numpy as np
import numpy.linalg as la

U, S, Vt = la.svd(A, full_matrices=False)

small_sig = []
small_vecs = []
related_columns = []

# Enter your code here
for i in range(len(S)):
    if S[i] <= 0.05:
        small_sig.append(S[i])
        small_vecs.append(Vt[i])
        related_list = []
        for j in range(len(Vt[i])):
            if np.abs(Vt[i][j]) > 0.1:
                related_list.append(column_names[j])
        related_columns.append(related_list)

# This code will print the groups of columns that you have found to be related
for entry in related_columns:
    print(entry)