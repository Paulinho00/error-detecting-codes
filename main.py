import numpy as np

import errorDetectingCodes

if __name__ == '__main__':
    crc = errorDetectingCodes.LongitudinalRedundancyCheck()
    array = np.random.randint(0, 2, 16)
    'array = np.array([0, 1, 1, 0, 1, 0, 0, 0, 0, 0])'
    print(array)
    array = crc.encode(array)
    print(array)
    print(crc.check(array))


