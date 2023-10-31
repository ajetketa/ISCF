import repository as rep
import feature as f
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

headers = ["HP", "IRDE", "IRFE", "IRBA", "BDE", "BFE", "BBA", "OR3DE", "OR3FE", "OR3BA", "OR6DE", "OR6FE", "OR6BA", "OR12DE", "OR12FE", "OR12BA", "Diameter"]

def import_data():
    sampleMatrix = rep.import_data()
    mean = f.variance(sampleMatrix)
    print("Mean")
    print(np.shape(mean))
    print(mean)
    table = tabulate(mean, headers)
    print(table)

    plt.plot(mean[:, 13], marker='o')
    plt.show()


if __name__ == '__main__':
    import_data()

