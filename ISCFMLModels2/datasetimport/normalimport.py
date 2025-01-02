import os
import numpy as np

normal_dir = "../full/normal"
noOfSensors = 8

def import_normal_data():
    count = 0
    for subdir, dirs, files in os.walk(normal_dir):
        for file in files:
            count += 1

    imbalance_data = np.empty((count, 9, 250000))

    index = 0
    for subdir, dirs, files in os.walk(normal_dir):
        for file in files:
            print(os.path.join(subdir, file))
            data = np.genfromtxt(os.path.join(subdir, file), delimiter=',', dtype=float)
            for i in range(0, noOfSensors):
                imbalance_data[index, i] = data[:, i]
            imbalance_data[index, noOfSensors] = 0
            index += 1

    np.save("../full/normal_data.npy", imbalance_data)