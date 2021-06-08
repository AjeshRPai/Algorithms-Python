def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    max_reach = array[0]
    steps = array[0]

    for i in range(1, len(array) - 1):
        max_reach = max(max_reach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i
    return jumps + 1


if __name__ == '__main__':
    array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
    array_2 = [3, 4, 2, 1, 5]
    print(minNumberOfJumps(array))
    print(minNumberOfJumps(array_2))

