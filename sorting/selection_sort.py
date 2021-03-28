def swap_array(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array


def selection_sort(array):
    for i in range(len(array)):
        lowest_value_index = i
        lowest_value = array[i]
        for j in range(i + 1, len(array)):
            if lowest_value > array[j]:
                lowest_value = array[j]
                lowest_value_index = j
        swap_array(array, i, lowest_value_index)
    return array


if __name__ == '__main__':
    print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
