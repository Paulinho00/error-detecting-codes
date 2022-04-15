import numpy as np

import errorDetectingCodes

if __name__ == '__main__':
    crc = errorDetectingCodes.CyclicRedundancyCheck()
    array = np.random.randint(0, 2, 10)
    'array = np.array([0, 1, 1, 0, 1, 0, 0, 0, 0, 0])'
    print(array)
    array = crc.encode(array)
    array[5] = 1
    array[7] = 1
    print(array)
    print(crc.check(array))


