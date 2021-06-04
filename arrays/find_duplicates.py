def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1


if __name__ == '__main__':
    array = [2, 3, 4, 2, 4, 5]
    print(firstDuplicateValue(array))
