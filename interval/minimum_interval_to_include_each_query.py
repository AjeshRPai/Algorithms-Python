from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Step 1: Sort intervals by start time
        intervals.sort()

        # Initialize variables
        min_heap = []  # Will store (interval_length, end_time)
        query_results = {}
        interval_idx = 0

        # Process each query in sorted order
        for query in sorted(queries):
            # Add all intervals that start before or at current query
            while (interval_idx < len(intervals) and
                   intervals[interval_idx][0] <= query):
                start, end = intervals[interval_idx]
                length = end - start + 1
                heapq.heappush(min_heap, (length, end))
                interval_idx += 1

            # Remove intervals that end before current query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # Get result for current query
            query_results[query] = min_heap[0][0] if min_heap else -1

        # Return results in original query order
        return [query_results[q] for q in queries]


# Driver code with multiple test scenarios
def test_min_interval():
    solution = Solution()

    # Test Case 1: Basic case
    intervals1 = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries1 = [2, 3, 4, 5]
    print("Test Case 1:")
    print(f"Intervals: {intervals1}")
    print(f"Queries: {queries1}")
    print(f"Result: {solution.minInterval(intervals1, queries1)}")  # Expected: [3,3,1,4]

    # Test Case 2: No valid intervals
    intervals2 = [[2, 3], [2, 5], [1, 8], [20, 25]]
    queries2 = [2, 19, 5, 22]
    print("\nTest Case 2:")
    print(f"Intervals: {intervals2}")
    print(f"Queries: {queries2}")
    print(f"Result: {solution.minInterval(intervals2, queries2)}")  # Expected: [2,-1,4,6]

    # Test Case 3: Overlapping intervals
    intervals3 = [[1, 4], [1, 4], [1, 4], [1, 4]]
    queries3 = [2, 3, 4, 5]
    print("\nTest Case 3:")
    print(f"Intervals: {intervals3}")
    print(f"Queries: {queries3}")
    print(f"Result: {solution.minInterval(intervals3, queries3)}")  # Expected: [4,4,4,-1]


if __name__ == "__main__":
    test_min_interval()