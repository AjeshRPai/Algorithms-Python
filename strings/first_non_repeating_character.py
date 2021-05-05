def firstNonRepeatingCharacter(string):
    index_map = {}
    for index in range(0, len(string)):
        if index_map.__contains__(string[index]):
            index_map[string[index]] += 1
        else:
            index_map[string[index]] = 1

    for index in range(0, len(string)):
        if index_map[string[index]] == 1:
            return index

    return -1


if __name__ == '__main__':
    print(firstNonRepeatingCharacter("abcdcaf"))
