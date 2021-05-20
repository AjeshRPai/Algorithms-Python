def sortKSortedArray(array,k):
    min_heap_with_k_elements = MinHeap(array[:min(k+1,len(array))])

    next_index_to_insert_element = 0

    for index in range(k+1,len(array)):
        min_element = min_heap_with_k_elements.remove()
        array[next_index_to_insert_element] = min_element
        next_index_to_insert_element+=1

        current_element = array[index]
        min_heap_with_k_elements.insert(current_element)

    while not min_heap_with_k_elements.isEmpty():
        min_element = min_heap_with_k_elements.remove()
        array[next_index_to_insert_element] = min_element
        next_index_to_insert_element+=1

    return array

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # input will be an array
    def buildHeap(self, array):
        # Write your code here.
        first_parent_index = (len(array) - 2) // 2
        for current_index in reversed(range(first_parent_index + 1)):
            self.siftDown(current_index, len(array) - 1, array)
        return array

    # move the value down
    def siftDown(self, current_index, end_index, heap):
        child_one_index = current_index * 2 + 1
        while child_one_index <= end_index:
            # if only one child is there
            # otherwise it child two is there then compare which one is lower
            child_two_index = current_index * 2 + 2 if current_index * 2 + 2 <= end_index else -1
            if child_two_index != -1 and heap[child_two_index] < heap[child_one_index]:
                index_to_swap = child_two_index
            else:
                index_to_swap = child_one_index

            if heap[index_to_swap] < heap[current_index]:
                self.swap(current_index, index_to_swap, heap)
                # already swapped
                current_index = index_to_swap
                child_one_index = current_index * 2 + 1
            else:
                # this means that the current heap or root is in correct condition
                return

                # move the value up

    def siftUp(self, current_index, heap):
        parent_index = (current_index - 1) // 2
        while current_index > 0 and heap[current_index] < heap[parent_index]:
            self.swap(current_index, parent_index, heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    # returns the minimum value or root .
    # since root will contain minimum value
    def peek(self):
        return self.heap[0]

    # Removes the root value or minimum value
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    # insert value
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def isEmpty(self):
        return len(self.heap)==0


if __name__ == '__main__':
    array = [3, 2,1, 5, 4, 7, 6, 5]
    k =3
    k_sorted_array = sortKSortedArray(array, k)
    print(k_sorted_array)
