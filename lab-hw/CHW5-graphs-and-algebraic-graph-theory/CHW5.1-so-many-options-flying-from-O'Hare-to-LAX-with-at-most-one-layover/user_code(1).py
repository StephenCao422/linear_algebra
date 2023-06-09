import numpy as np
import numpy.linalg as la

# print(nonstop_flights)
atmost_1_layover = nonstop_flights + nonstop_flights @ nonstop_flights
num_options = atmost_1_layover[63][22]