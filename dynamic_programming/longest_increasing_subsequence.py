def longestIncreasingSubsequence(array):
    sequence = [None] * len(array)
    lengths = [1 for x in array]
    sequence[0] = 1
    max_sequence_index = 0

    for index_1 in range(len(array)):
        for index_2 in range(0,index_1):
            first_number = array[index_1]
            second_number = array[index_2]
            if second_number < first_number and lengths[index_2] + 1 >= lengths[index_1]:
                lengths[index_1] = lengths[index_2] + 1
                sequence[index_1] = index_2
        if lengths[index_1] >= lengths[max_sequence_index]:
            max_sequence_index = index_1

    print(max_sequence_index)
    print("sequence",sequence)
    print("current index",max_sequence_index)
    print(lengths)

    return buildSequence(array,sequence,max_sequence_index)

def buildSequence(array,sequences,current_index):
    sequence = []
    while current_index is not None:
        sequence.append(array[current_index])
        current_index = sequences[current_index]
    return list(reversed(sequence))


if __name__ == '__main__':
    array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
    result = longestIncreasingSubsequence(array)
    print(result)
