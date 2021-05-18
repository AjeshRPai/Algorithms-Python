class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC,[])
        self.greaters = Heap(MIN_HEAP_FUNC,[])
        self.median = None

    def insert(self, number):
        if not self.lowers.length or number<self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalance_heaps()
        self.update_median()

    def getMedian(self):
        return self.median

    def rebalance_heaps(self):
        if self.lowers.length - self.greaters.length ==2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length ==2:
            self.lowers.insert(self.greaters.remove())

    def update_median(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek()+self.greaters.peek())/2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

class Heap:
    def __init__(self, comparison_function,array):
        self.comparison_function = comparison_function
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

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
            if child_two_index != -1:
                if self.comparison_function(heap[child_two_index], heap[child_one_index]):
                    index_to_swap = child_two_index
                else:
                    index_to_swap = child_one_index
            else:
                index_to_swap = child_one_index

            if self.comparison_function(heap[index_to_swap], heap[current_index]):
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
        while current_index > 0:
            if self.comparison_function(heap[current_index], heap[parent_index]):
                self.swap(current_index, parent_index, heap)
                current_index = parent_index
                parent_index = (current_index - 1) // 2
            else:
                return

    # returns the minimum value or root .
    # since root will contain minimum value
    def peek(self):
        return self.heap[0]

    # Removes the root value or minimum value
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.length-=1
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    # insert value
    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

def MAX_HEAP_FUNC(a,b):
    return a>b

def MIN_HEAP_FUNC(a,b):
    return a<b


if __name__ == '__main__':
    median = ContinuousMedianHandler()
    median.insert(2)
    median.insert(3)
    median.insert(4)
    median.insert(5)
    print(median.getMedian())
