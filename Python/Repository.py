import scipy

sampleRate12k = []
sampleRate48k = []
normal = []

fileStartingNames = ['IR', 'B', 'OR']
possibleDiameters = ['007', '014', '021', '028']
possibleHP = ['0', '1', '2', '3']
possibleHours = ['6', '3', '12']

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
        return revisedFile
    except:
        print(f"{fileName} does not exist on the given folder: {folderName}")

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
# CAUTION: if DE_time, or FE_time or BA_time will not be given the respective index will be missing from the map
# CAUTION: if data for a specific clock will be missing for OR the clock number will appear but the data will be replaced with None
def import_data():
    for diameter in possibleDiameters:
        for hp in possibleHP:
            dataObject = {}
            dataObject["HP"] = int(hp)
            dataObject["Diameter"] = float("0." + diameter)
            for fileStartingName in fileStartingNames:
                fileName = fileStartingName + diameter
                if fileStartingName == 'OR':
                    outerRace = {}
                    for possibleHour in possibleHours:
                        file = fileName + '@' + possibleHour + '_' + hp
                        outerRace[possibleHour] = load_data("12kSampleRate", file)
                    dataObject[fileStartingName] = outerRace
                else:
                    file = fileName + '_' + hp
                    dataObject[fileStartingName] = load_data("12kSampleRate", file)

            sampleRate12k.append(dataObject)

    return sampleRate12k