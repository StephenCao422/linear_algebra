import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

covid_avg = np.average(covid_global, axis=0)
covid_center = covid_global - covid_avg
U, S, Vt = la.svd(covid_center, full_matrices=False)
V = Vt.T
comp_basis = (covid_comp - covid_avg) @ V
global_basis = covid_center @ V
diff_arr = []
for row in global_basis:
    diff_arr.append(la.norm(row - comp_basis))
differences = np.array(diff_arr)

# uncomment below to print the global outbreaks by similarity to the comparison country
# ordering is most-similar to least-similar
#print([name for _,name in sorted(zip(differences,names_global),key=lambda p: p[0])])

# uncomment below to visualize your PCA
#display_pca(V, comp_basis, global_basis)