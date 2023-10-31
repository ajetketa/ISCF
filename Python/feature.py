import numpy as np
import repository as r

def mean(dataSample):
    mean = np.empty((r.possibleMatrixLength[r.database], 17))
    for i in range(np.shape(dataSample)[0]):
        for j in range(np.shape(dataSample)[1]):
            if j >= 1 and j <= np.shape(dataSample)[1] - 1:
                data = dataSample[i, j]
                mask = ~np.isnan(data)
                if data[mask] is not None and np.shape(data[mask])[0] == 0:
                    mean[i, j] = None
                else:
                    mean[i, j] = np.mean(data[mask])
            else:
                mean[i, j] = dataSample[i, j, 0, 0]

    return mean

def variance(dataSample):
    variance = np.empty((r.possibleMatrixLength[r.database], 17))
    for i in range(np.shape(dataSample)[0]):
        for j in range(np.shape(dataSample)[1]):
            if j >= 1 and j <= np.shape(dataSample)[1] - 1:
                data = dataSample[i, j]
                mask = ~np.isnan(data)
                if data[mask] is not None and np.shape(data[mask])[0] == 0:
                    variance[i, j] = None
                else:
                    variance[i, j] = np.var(data[mask])
            else:
                variance[i, j] = dataSample[i, j, 0, 0]

    return variance






