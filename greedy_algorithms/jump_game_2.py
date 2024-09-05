from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= goal:
                goal = index
        return goal == 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.jump(nums= [1, 2, 0, 1, 0]))