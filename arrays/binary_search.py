from typing import List


def search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1

    while start <= end:
        middle = start + ((end - start) // 2)
        if target > nums[middle]:
            start = middle + 1
        elif target < nums[middle]:
            end = middle - 1
        else:
            return middle

    return -1


if __name__ == '__main__':
    print(search([-1, 0, 2, 4, 6, 8, 9], 4))
    print(search([-1, 0, 2, 4, 6, 8], 3))
