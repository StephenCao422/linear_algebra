import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

plt.figure()
plt.imshow(image, cmap='gray')
print(image.shape)
compressed = image.copy()

## Add your code here
D = create_dct_basis(8) # 8 x 8
def compress_chunk(chunk):
    print
    converted = D.T @ chunk @ D
    threshold = np.abs(converted).max() *0.1
    for i in range (8):
        for j in range (8):
            if (abs(converted[i][j]) < threshold):
                converted[i][j] = 0
    squished = D @ converted @ D.T
    clipped = np.clip(squished, 0, 255)
    return clipped
    

N = 8
for u in range(0, image.shape[0], N):
    for v in range(0, image.shape[1], N):
        compressed[u:u+N, v:v+N] = compress_chunk(image[u:u+N, v:v+N])
#compressed = compress_chunk(image)
plt.figure()
plt.imshow(compressed, cmap='gray')