from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            print("dfs of i called", i)
            if i >= len(nums):
                print("subset copy", subset.copy())
                res.append(subset.copy())
                return
            print("nums i ",nums[i])
            subset.append(nums[i])
            print("subset after append", subset)
            dfs(i + 1)


            subset.pop()
            print("after subset is popped", subset)
            dfs(i + 1)

        dfs(0)
        return res


# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


if __name__ == '__main__':
    solution = Solution()
    res = solution.subsets([1, 2, 3, 4, 5])
    print(res)
