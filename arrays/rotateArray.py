from typing import List

from collections import defaultdict


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n  # In case k is greater than n
    nums[:] = nums[-k:] + nums[:-k]


#Driver code
if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,7]
    nums2 = [5,6,7,1,2,3,4]
    k = 3
    rotate(nums1,k)
    print(nums1==nums2)
    print(k)
