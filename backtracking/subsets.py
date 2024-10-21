from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


if __name__ == '__main__':
    solution = Solution()
    res = solution.subsets([1, 2, 3, 4, 5])
    nums1 = [1, 2, 3]
    nums2 = [0]
    nums3 = []
    nums4 = [1, 2]

    # Driver code to test the function
    print("Subsets of [1, 2, 3]:", solution.subsets(nums1))
    print("Subsets of [0]:", solution.subsets(nums2))
    print("Subsets of [] (empty set):", solution.subsets(nums3))
    print("Subsets of [1, 2]:", solution.subsets(nums4))
