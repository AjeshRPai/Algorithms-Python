def hasSingleCycle(array):
    number_of_jumps = 0
    current_index = 0

    while number_of_jumps < len(array):
        if number_of_jumps > 0 and current_index == 0:
            return False
        number_of_jumps += 1
        current_index = getNextIndex(array, current_index)
    return current_index == 0


def getNextIndex(array, curren_index):
    jump = array[curren_index]
    next_index = (curren_index + jump) % len(array)
    return next_index if next_index >= 0 else len(array)


if __name__ == '__main__':
    print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
