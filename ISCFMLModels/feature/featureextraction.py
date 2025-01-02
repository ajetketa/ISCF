import numpy as np
from scipy.stats import skew, kurtosis

class Feature:
    def __init__(self, dataset):
        self.dataset = dataset

    def mean(self):
        mean = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                mean[i, j] = np.mean(self.dataset[i, j])
            mean[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]

        return mean

    def variance(self):
        variance = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                variance[i, j] = np.var(self.dataset[i, j])
            variance[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]

        return variance

    def kurtosis(self):
        kurtosisNp = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                kurtosisNp[i, j] = kurtosis(self.dataset[i, j])
            kurtosisNp[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]

        return kurtosisNp

    def skewness(self):
        skewNp = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                skewNp[i, j] = skew(self.dataset[i, j])
            skewNp[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]

        return skewNp
