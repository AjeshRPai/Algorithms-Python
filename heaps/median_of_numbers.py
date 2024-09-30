import heapq

class MedianFinder:
    def __init__(self):
        # max_heap is a max heap for the smaller half of the numbers.
        # Python's heapq implements a min heap, so we store negative values to simulate a max heap.
        self.max_heap = []  # Stores the smaller half of numbers (negated to use as max heap).

        # min_heap is a min heap for the larger half of the numbers.
        self.min_heap = []  # Stores the larger half of numbers.

    def addNum(self, num: int) -> None:
        # Step 1: Always push the new number to max_heap first (negate to simulate max heap behavior).
        heapq.heappush(self.max_heap, -num)

        # Step 2: Ensure the max element in max_heap is <= min element in min_heap (balance the heaps).
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            # Move the largest element from max_heap to min_heap to maintain order.
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)

        # Step 3: Balance the heaps if they have unequal sizes.
        # If max_heap has more than 1 extra element compared to min_heap:
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move the top element from max_heap to min_heap.
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)

        # If min_heap has more elements than max_heap:
        elif len(self.min_heap) > len(self.max_heap):
            # Move the top element from min_heap to max_heap.
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)

    def findMedian(self) -> float:
        # If the max_heap has more elements, the median is the top element of max_heap.
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]

        # If both heaps are the same size, the median is the average of the two tops.
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# Testing the MedianFinder with different scenarios

# Helper function to test a list of inputs
def test_median_finder(numbers):
    median_finder = MedianFinder()
    print(f"Adding numbers: {numbers}")

    for num in numbers:
        median_finder.addNum(num)
        median = median_finder.findMedian()
        print(f"Added {num}, current median: {median}")
    print("-" * 40)


if __name__ == '__main__':
    # Test case 1: Odd number of elements
    test_median_finder([1, 2, 3, 4, 5])  # Expected median progression: 1, 1.5, 2, 2.5, 3

    # Test case 2: Even number of elements
    test_median_finder([5, 10, 15, 20])  # Expected median progression: 5, 7.5, 10, 12.5

    # Test case 3: Negative numbers
    test_median_finder([-5, -10, -15, -20])  # Expected median progression: -5, -7.5, -10, -12.5

    # Test case 4: Mixed positive and negative numbers
    test_median_finder([10, -1, 7, -3, 5])  # Expected median progression: 10, 4.5, 7, 3.0, 5

    # Test case 5: Duplicates
    test_median_finder([2, 2, 2, 2, 2])  # Expected median progression: 2, 2, 2, 2, 2
