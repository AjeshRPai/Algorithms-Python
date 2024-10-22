import heapq

class Solution:
    def furthest_building(self, heights, ladders, bricks):
        height_diff_heap = []

        for i in range(len(heights) - 1):
            height_diff = heights[i + 1] - heights[i]

            if height_diff > 0:
                heapq.heappush(height_diff_heap, height_diff)

            if len(height_diff_heap) > ladders:
                bricks -= heapq.heappop(height_diff_heap)

            if bricks < 0:
                return i

        return len(heights)-1


if __name__ == '__main__':
    # Test cases
    test_cases = [
        {
            "heights": [4, 2, 7, 6, 9, 14, 12],
            "bricks": 5,
            "ladders": 1,
            "expected": 4
        },
        {
            "heights": [4, 12, 2, 7, 3, 18, 20, 3, 19],
            "bricks": 10,
            "ladders": 2,
            "expected": 7
        },
        {
            "heights": [14, 3, 19, 3],
            "bricks": 17,
            "ladders": 0,
            "expected": 3
        },
        {
            "heights": [1, 2, 3, 4, 5],
            "bricks": 10,
            "ladders": 0,
            "expected": 4
        },
        {
            "heights": [1, 5, 1, 2, 3, 4],
            "bricks": 3,
            "ladders": 2,
            "expected": 5
        },
        {
            "heights": [1, 3, 5, 6],
            "bricks": 2,
            "ladders": 1,
            "expected": 3
        }
    ]

    solution = Solution()

    # Test the function on all test cases
    for i, test_case in enumerate(test_cases):
        heights = test_case["heights"]
        bricks = test_case["bricks"]
        ladders = test_case["ladders"]
        expected = test_case["expected"]

        # Call the solution function
        result = solution.furthest_building(heights, bricks, ladders)

        # Compare the result with the expected output
        if result == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed (Expected {expected}, got {result})")


