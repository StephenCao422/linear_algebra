import numpy as np

# Write your code to calculate T below this line
S_vec = np.array([S[0]+S[1]+S[8], S[2], S[7]+S[8], S[3]+S[4], S[5]+S[6]])
print(S_vec.shape)
t_np = np.array(
[[4, -1, 0, 0, 0],
[-1,4,-1,-1,0],
[0,-1,4,0,-1],
[0,-1,0,4,-1],
[0,0,-1,-1,4]
    ]    
    )
T= np.linalg.inv(t_np) @ S_vec.T