# boundary conditions.
# takes array of integers. It can be negative or zero also
# can contain duplicate values

# pseudo code
# take items from unsorted part and move to first(sorted)
#
def insertion_sort(array):
    for i in range(len(array)):
        print(array[i])
        position_to_insert = i
        value_to_insert = array[i]
        while position_to_insert > 0 and array[position_to_insert - 1] > value_to_insert:
            array[position_to_insert] = array[position_to_insert - 1]
            position_to_insert = position_to_insert - 1
        array[position_to_insert] = value_to_insert
    return array


if __name__ == '__main__':
    print(insertion_sort([8, 5, 2, 9, 5, 6, 3]))
