import numpy as np


def parity_check_encode(array: np.ndarray) -> np.ndarray:
    number_of_ones = 0
    for element in array:
        if element:
            number_of_ones += 1
    if number_of_ones % 2 == 0:
        return np.append(array, 0)
    else:
        return np.append(array, 1)


def parity_check_decode(array: np.ndarray) -> bool:
    number_of_ones = 0
    for element in array:
        if element:
            number_of_ones += 1
    if number_of_ones % 2 == 0:
        return True
    else:
        return False


class CyclicRedundancyCheck:
    def __init__(self):
        self.__polynomial = np.array([1, 1, 0, 0, 1, 1, 0, 0, 1])
        self.__number_of_bits = 9

    def encode(self, array):
        data_array = np.append(array, np.full(self.__number_of_bits, 0))
        integer_value_of_array = data_array.dot(2 ** np.arange(data_array.size)[::-1])
        divisor = np.append(self.__polynomial, np.full(data_array.size - self.__polynomial.size, 0))
        integer_value_of_divisor = divisor.dot(2**np.arange(divisor.size)[::-1])

        while integer_value_of_array > (2 ** self.__number_of_bits - 1):
            if integer_value_of_divisor <= ((2 ** (np.floor(np.log2(integer_value_of_array))+1)) - 1):
                integer_value_of_array = integer_value_of_array ^ integer_value_of_divisor
            integer_value_of_divisor = integer_value_of_divisor >> 1

        crc_code = np.fromstring(np.binary_repr(integer_value_of_array).zfill(3), dtype='S1').astype(int)
        return np.append(array, crc_code)

    def check(self, array):
        integer_value_of_array = array.dot(2 ** np.arange(array.size)[::-1])
        divisor = np.append(self.__polynomial, np.full(array.size - self.__polynomial.size, 0))
        integer_value_of_divisor = divisor.dot(2**np.arange(divisor.size)[::-1])

        while integer_value_of_array > (2 ** self.__number_of_bits - 1):
            if integer_value_of_divisor <= ((2 ** (np.floor(np.log2(integer_value_of_array))+1)) - 1):
                integer_value_of_array = integer_value_of_array ^ integer_value_of_divisor
            integer_value_of_divisor = integer_value_of_divisor >> 1

        if integer_value_of_array == 0:
            return True
        else:
            return False
