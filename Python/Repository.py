import scipy
import constant as c
import numpy as np

fileStartingNames = ['IR', 'B', 'OR']
possibleDiameters = {
    "12kSampleRate": ['007', '014', '021', '028'],
    "48kSampleRate": ['007', '014', '021'],
    "FanEndBearingFault": ['007', '014', '021']
}
possibleHP = ['0', '1', '2', '3']
possibleHours = ['6', '3', '12']
possibleMatrixLength = {
    "12kSampleRate": 16,
    "48kSampleRate": 12,
    "FanEndBearingFault": 12
}

database = "12kSampleRate" # Change Based on Database you want to import (12kSampleRate, 48kSampleRate, FanEndBearingFault)

# DE_time == Array Index 0
# FE_time == Array Index 1
# BA_time == Array Index 2
def load_data(folderName, fileName):
    root = "../Database"
    try:
        file = scipy.io.loadmat(f"../Database/{folderName}/{fileName}", appendmat=True)
        revisedFile = {}
        for key in file:
            if "DE_time" in key:
                revisedFile[0] = file[key]
            if "FE_time" in key:
                revisedFile[1] = file[key]
            if "BA_time" in key:
                revisedFile[2] = file[key]
        for i in range(3):
            if i not in revisedFile:
                revisedFile[i] = None
        return revisedFile
    except:
        print(f"{fileName} does not exist on the given folder: {folderName}")

# Find max length over all the given signals (necessary for padding and array initialization)
def find_max_length(data, currentMaxLength):
    if data is None: return currentMaxLength
    for (key, value) in data.items():
        if value is not None and len(value) > currentMaxLength:
            currentMaxLength = len(value)
    return currentMaxLength

# Pad the rows of the given array up until paddLength starting from the last value of the array
# with the mean of the entire array
def padded_array(array, paddLength):
    if array is None: return None
    return np.pad(np.array(array),((0, paddLength - len(array)), (0, 0)), "mean")

# Transforms the given dictionary to a matrix of values
# Each row represents a measurement
# Each column represents the following:
# 0 : HP
# 1 : Inner Ring DE Time
# 2 : Inner Ring FE Time
# 3 : Inner Ring BA Time
# 4 : Ball DE Time
# 5 : Ball FE Time
# 6 : Ball BA Time
# 7 : Outer Ring 3 o'clock DE Time
# 8 : Outer Ring 3 o'clock FE Time
# 9 : Outer Ring 3 o'clock BA Time
# 10 : Outer Ring 6 o'clock DE Time
# 11 : Outer Ring 6 o'clock FE Time
# 12 : Outer Ring 6 o'clock BA Time
# 13 : Outer Ring 12 o'clock DE Time
# 14 : Outer Ring 12 o'clock FE Time
# 15 : Outer Ring 12 o'clock BA Time
# 16 : Fault Diameter
def get_matrix(dataSet):
    maxLength = 0
    for (index, data) in enumerate(dataSet):
        maxLength = max(maxLength,
                        find_max_length(data[c.innerRing], maxLength),
                        find_max_length(data[c.ball], maxLength),
                        find_max_length(data[c.outerRing]["3"], maxLength),
                        find_max_length(data[c.outerRing]["6"], maxLength),
                        find_max_length(data[c.outerRing]["12"], maxLength),
                        )

    shape = [possibleMatrixLength[database], 17, maxLength, 1]
    array = np.empty(shape)

    for (index, data) in enumerate(dataSet):
        array[index, 0] = data[c.hp]
        array[index, 1] = padded_array(data[c.innerRing][0], maxLength)
        array[index, 2] = padded_array(data[c.innerRing][1], maxLength)
        array[index, 3] = padded_array(data[c.innerRing][2], maxLength)
        array[index, 4] = padded_array(data[c.ball][0], maxLength)
        array[index, 5] = padded_array(data[c.ball][1], maxLength)
        array[index, 6] = padded_array(data[c.ball][2], maxLength)

        if data[c.outerRing]["3"] is not None:
            array[index, 7] = padded_array(data[c.outerRing]["3"][0], maxLength)
            array[index, 8] = padded_array(data[c.outerRing]["3"][1], maxLength)
            array[index, 9] = padded_array(data[c.outerRing]["3"][2], maxLength)
        else:
            array[index, 7] = None
            array[index, 8] = None
            array[index, 9] = None

        if data[c.outerRing]["6"] is not None:
            array[index, 10] = padded_array(data[c.outerRing]["6"][0], maxLength)
            array[index, 11] = padded_array(data[c.outerRing]["6"][1], maxLength)
            array[index, 12] = padded_array(data[c.outerRing]["6"][2], maxLength)
        else:
            array[index, 10] = None
            array[index, 11] = None
            array[index, 12] = None

        if data[c.outerRing]["12"] is not None:
            array[index, 13] = padded_array(data[c.outerRing]["12"][0], maxLength)
            array[index, 14] = padded_array(data[c.outerRing]["12"][1], maxLength)
            array[index, 15] = padded_array(data[c.outerRing]["12"][2], maxLength)
        else:
            array[index, 13] = None
            array[index, 14] = None
            array[index, 15] = None

        array[index, 16] = data[c.diameter]

    return array

# A dataObject will be a row with all possible data for a given Diameter and HP combination
# Example:
# dataObject = {
#     "Diameter": float,
#     "HP": int,
#     "IR": {
#          0 (DE_time): [],
#          1 (FE_time): [],
#          2 (BA_time): []
#      },
#     "B": Same structure as IR
#     "OR": {
#          "3" (at 3 o'clock): same structure as IR
#          "6" (at 6 o'clock): same structure as IR
#          "12" (at 12 o'clock): same structure as IR
#      }
# }
# CAUTION: if DE_time, or FE_time or BA_time will not be given the respective index will not be missing but will be replaced with None
# CAUTION: if data for a specific clock will be missing for OR the clock number will appear but the data will be replaced with None
def import_data():
    sampleRate = []
    for diameter in possibleDiameters[database]:
        for hp in possibleHP:
            dataObject = {}
            dataObject[c.hp] = int(hp)
            dataObject[c.diameter] = float("0." + diameter)
            for fileStartingName in fileStartingNames:
                fileName = fileStartingName + diameter
                if fileStartingName == c.outerRing:
                    outerRace = {}
                    for possibleHour in possibleHours:
                        file = fileName + '@' + possibleHour + '_' + hp
                        outerRace[possibleHour] = load_data(database, file)
                    dataObject[fileStartingName] = outerRace
                else:
                    file = fileName + '_' + hp
                    dataObject[fileStartingName] = load_data(database, file)
            sampleRate.append(dataObject)

    return get_matrix(sampleRate)
