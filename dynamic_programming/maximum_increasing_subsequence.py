def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


def maxSumIncreasingSubsequence(array):
    print(array)
    sums = [num for num in array]
    combinations_for_each_index = [[x for x in array]] * len(array)

    sums[0] = array[0]
    combinations_for_each_index[0] = [array[0]]

    maximum_sum_index = 0
    maximum_sum = array[0]

    for index_2 in range(1, len(array)):
        for index_1 in range(0, index_2):
            calculated_value = array[index_2] + sums[index_1]
            if array[index_2] > array[index_1] and calculated_value >= sums[index_2]:
                current_value = array[index_2]
                sums[index_2] = max(calculated_value, current_value)

                if calculated_value > current_value:
                    combination = flatten(combinations_for_each_index[index_1])
                    combination.append(array[index_2])
                    combinations_for_each_index[index_2] = combination
            else:
                combinations_for_each_index[index_2] = [array[index_2]]

        if sums[index_2] > maximum_sum:
            maximum_sum = sums[index_2]
            maximum_sum_index = index_2

    print("value for each", sums)
    print(combinations_for_each_index)
    print(maximum_sum)
    print(maximum_sum_index)

    print(flatten(combinations_for_each_index[maximum_sum_index]))
    return maximum_sum, flatten(combinations_for_each_index[maximum_sum_index])


def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = [num for num in array]

    maximum_sum_index = 0

    for i in range(len(array)):
        current_number = array[i]
        for j in range(0, i):
            other_num = array[j]
            calculated_value = current_number + sums[j]
            if current_number > other_num and calculated_value >= sums[i]:
                sums[i] = max(calculated_value, current_number)
                sequences[i] = j

        if sums[i] > sums[maximum_sum_index]:
            maximum_sum_index = i

    return [sums[maximum_sum_index],buildSequence(array,sequences,maximum_sum_index)]

def buildSequence(array,sequences,current_index):
    sequence = []
    while current_index is not None:
        sequence.append(array[current_index])
        current_index = sequences[current_index]
    return list(reversed(sequence))


if __name__ == '__main__':
    test_case1 = [10, 70, 20, 30, 50, 11, 30]
    test_case2 = [-5, -4, -3, -1]
    # test_case3 = [8, 12, 2, 3, 15, 5, 7]
    # test_case4 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(maxSumIncreasingSubsequence(test_case1))
    print(maxSumIncreasingSubsequence(test_case2))
    # print(maxSumIncreasingSubsequence(test_case3))
    # print(maxSumIncreasingSubsequence(test_case4))
