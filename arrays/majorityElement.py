from typing import List

from collections import defaultdict

def majorityElement(nums: List[int]) -> int:
    majority = len(nums) // 2
    print(majority)
    majorityDict = defaultdict(int)

    for i in range(len(nums)):
        majorityDict[nums[i]] += 1
        if majorityDict[nums[i]] > majority:
            return nums[i]

    print(majorityDict)

# Driver Code
if __name__ == "__main__":
    nums1 = [3, 2, 3]
    k = majorityElement(nums1)
    print(nums1)
    print(k)
