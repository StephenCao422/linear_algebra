import numpy as np

# write your code here
A = np.array([[0, 3], [2, 1]])
A_inv = np.linalg.inv(A)
corrected = A_inv @ image

# You can use the function "display_image" to display your result
display_image(image)
display_image(corrected)