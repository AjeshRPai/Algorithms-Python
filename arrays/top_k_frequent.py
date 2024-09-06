from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each element
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1


        print(count)

        # Step 2: Create a list of buckets to group numbers by their frequency
        # The index of each sublist represents the frequency of numbers in that sublist
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        print(freq)

        # Step 3: Collect the top k frequent elements
        result = []
        # Iterate from the highest frequency to the lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                # Stop when we've collected k elements
                if len(result) == k:
                    return result

if __name__ == '__main__':
    solution = Solution()
    solution.topKFrequent(nums = [1,2,2,3,3,3], k = 2)