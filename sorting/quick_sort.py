def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
# Function to do Quick sort

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        print(arr)
        print(pi)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr


def quickSort3(arr):
    if len(arr) <= 1:
        return arr

    partition = arr[0]

    less = [i for i in arr[1:] if i <= partition]
    greater = [i for i in array[1:] if i > partition]

    return quickSort3(less) + [partition] + quickSort3(greater)


if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    print(quickSort(array, 0, len(array) - 1))
    print(quickSort3(array))
