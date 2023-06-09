import os
import matplotlib.pyplot as plt
import numpy as np

base_path = 'att_faces'
unknown_file = 'unknown.pgm'

def load_normalized(file):
    return (plt.imread(file) / 255).astype(np.float64)

def load_face_dataset():
    files = []
    shape = None
    for directory in os.listdir(base_path):
        if directory in ['README', 'unknown.pgm']:
            continue
        for file in os.listdir(os.path.join(base_path, directory)):
            fname = os.path.join(base_path, directory, file)
            loaded = load_normalized(fname)
            if shape is None:
                shape = loaded.shape
            elif shape != loaded.shape:
                raise Exception(f'File {file} has different shape')
            files.append(load_normalized(fname).flatten())
    return (shape, files)

def load_unknown():
    return load_normalized(os.path.join(base_path, unknown_file)).flatten()
