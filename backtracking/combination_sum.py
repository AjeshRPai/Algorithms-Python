from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(indexOfNums, currentArray, total):
            # base case 1 - if the target is acheived, copy the current array and return it
            if total == target:
                res.append(currentArray.copy())
                return

            # if the number is more or the total target is more then return
            if indexOfNums >= len(nums) or total > target:
                return

            # the number is added to the array and then called for DFS
            currentArray.append(nums[indexOfNums])
            dfs(indexOfNums, currentArray, total + nums[indexOfNums])
            # when the above returns, then the last item in array is removed and called for dfs again
            currentArray.pop()
            dfs(indexOfNums + 1, currentArray, total)

        dfs(0, [], 0)
        return res



# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum(nums = [2,5,6,9] ,target = 9)
    print(res)
