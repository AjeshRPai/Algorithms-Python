def longestIncreasingSubsequence(array):
    sequence = [None for x in array]
    lengths = [1 for x in array]
    max_sequence_index = 0
    for index_1 in range(len(array)):
        first_number = array[index_1]
        for index_2 in range(0,index_1):
            second_number = array[index_2]
            if second_number < first_number and lengths[index_2] + 1 >= lengths[index_1]:
                lengths[index_1] = lengths[index_2] + 1
                sequence[index_1] = index_2
        if lengths[index_1] >= lengths[max_sequence_index]:
            max_sequence_index = index_1


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
