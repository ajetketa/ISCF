import os
import numpy as np

imbalance_dir = "../full/imbalance"
normal_dir = "../full/normal"
noOfSensors = 8

def import_imbalance_data():
    count = 0
    for subdir, dirs, files in os.walk(imbalance_dir):
        for file in files:
            count += 1

    imbalance_data = np.empty((count, 9, 250000))

    index = 0
    for subdir, dirs, files in os.walk(imbalance_dir):
        for file in files:
            print(os.path.join(subdir, file))
            directory_name = int(subdir[subdir.rindex('\\') + 1 : len(subdir) - 1])
            data = np.genfromtxt(os.path.join(subdir, file), delimiter=',', dtype=float)
            for i in range(0, noOfSensors):
                imbalance_data[index, i] = data[:, i]
            imbalance_data[index, noOfSensors] = directory_name
            index += 1

    np.save("../full/imbalance_data.npy", imbalance_data)





