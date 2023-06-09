import numpy as np

# This is your original image
display_image(image)

# modify the definition of the 'sheared' variable to apply the correct transformation
shear = np.array([[1, 0.8], [0, 1]])
sheared = shear @ image
display_image(sheared)

# modify the definition of the 'rotated' variable to apply the correct transformation
rotate = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)], [np.sin(np.pi/4), np.cos(np.pi/4)]])
rotated = rotate @ image
display_image(rotated)

# modify the definition of the 'sheared_and_rotated' variable to apply the correct transformation
sheared_and_rotated = rotate @ shear @ image
display_image(sheared_and_rotated)