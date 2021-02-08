# boundary conditions:
#     takes array of integers - can be negative and zero
#     can have duplicate elements

# pseudo code:
# Bubble sort
# iterate over the array
# swap the items one by one
# break condition for the loop
# if no swap is to be done then end the sort

# complexity:
# Best:O(n) time
# Average:O(n^2) time
# Worst:O(n^2) time |

def swap_array(array, i, j):
    array[i],array[j] = array[j],array[i]
    return array


def bubbleSort(array):
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array = swap_array(array, i, i + 1)
                is_sorted = False
    return array

if __name__ == '__main__':
    print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))
