from typing import List

def maxSubArray(nums: List[int]) -> int:
    res = nums[0]
    total = 0

    for num in nums:
        # add the number to the total as we have to compute the total anyways as we go forward with the array
        total += num
        # check if this total is more or the previous one and store it
        res = max(res, total)
        # if this total is less than zero then reset it to zero
        if total<0:
            total = 0
    return res

if __name__ == '__main__':
    maxSubArray([2,-3,4,-2,2,1,-1,4])

