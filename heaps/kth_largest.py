from typing import List


def findKthLargest(self, nums: List[int], k: int) -> int:
    k = len(nums) - k
    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k:
            return quickSelect(1, p - 1)
        elif p < k:
            return quickSelect(p + 1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums)-1)

if __name__ == '__main__':
    print(findKthLargest(nums=[2, 3, 1, 5, 6, 4], k=2))
    # expected 4
