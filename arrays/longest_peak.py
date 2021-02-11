def longestPeak(array):
    if len(array) < 3:
        return 0

    downward_slope = False
    length = 1
    max_length = 0

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            if downward_slope:
                max_length = max(max_length, length)
                length = 2
                downward_slope = False
            else:
                length += 1
        elif array[i] < array[i - 1]:
            if length >= 2:
                downward_slope = True

            if downward_slope:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1
        else:
            length = 1

    return max_length


if __name__ == '__main__':
    print('max_peak ' + longestPeak([5, 4, 3, 2, 1, 2, 1]).__str__())
