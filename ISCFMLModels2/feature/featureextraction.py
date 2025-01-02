import numpy as np
import gc
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
            gc.collect()
        return mean

    def variance(self):
        variance = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                variance[i, j] = np.var(self.dataset[i, j])
            variance[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]
            gc.collect()
        return variance

    def kurtosis(self):
        kurtosisNp = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                kurtosisNp[i, j] = kurtosis(self.dataset[i, j])
            kurtosisNp[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]
            gc.collect()
        return kurtosisNp

    def skewness(self):
        skewNp = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                skewNp[i, j] = skew(self.dataset[i, j])
            skewNp[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]
            gc.collect()
        return skewNp

    def energy(self):
        energy = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                energy[i, j] = np.sum(self.dataset[i, j] ** 2)
            energy[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]
            gc.collect()
        return energy

    def rms(self):
        rms = np.empty((np.shape(self.dataset)[0], np.shape(self.dataset)[1]))

        for i in range(np.shape(self.dataset)[0]):
            for j in range(np.shape(self.dataset)[1] - 1):
                rms[i, j] = np.sqrt(np.mean(self.dataset[i, j] ** 2))
            rms[i, np.shape(self.dataset)[1] - 1] = self.dataset[i, np.shape(self.dataset)[1] - 1, 0]
            gc.collect()
        return rms

