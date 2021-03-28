

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        # compare the ones from left array and right array
        # which ever one is smaller copy it into the final array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # if any element is left after the iteration
        # copy it to the final array
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array


if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    print(merge_sort(array))
