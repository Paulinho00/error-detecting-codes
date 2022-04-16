import numpy as np

import errorDetectingCodes

if __name__ == '__main__':
    crc = errorDetectingCodes.FletcherChecksum()
    array = np.random.randint(0, 2, 22)
    'array = np.array([0, 1, 1, 0, 1, 0, 0, 0, 0, 0])'
    print(array)
    array = crc.encode(array)
    array[0][0] = 1
    print(array)
    print(crc.check(array))

