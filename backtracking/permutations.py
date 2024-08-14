from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # if the length is 1, then return ?
        if len(nums) == 1:
            return [nums[:]]

        # look at the range of the nums and start with the first one
        for i in range(len(nums)):
            n = nums.pop(0)
            # remove the first number and
            # look at the perms of the rest recursively
            perms = self.permute(nums)

            # iterate through all the permutations
            for perm in perms:
                # add the removed value to each permutations
                perm.append(n)

            # add the perms to the end of result
            res.extend(perms)
            # add the num to the end of the list
            nums.append(n)
        return res







# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


if __name__ == '__main__':
    solution = Solution()
    res = solution.permute([1, 2, 3])
    print(res)
