from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize the result list to store all valid combinations
        result = []

        # Sort the candidates to handle duplicates more easily
        candidates.sort()

        # Helper function to perform Depth-First Search (DFS)
        def dfs(index, current_combination, current_sum):
            # If the current sum equals the target, add the combination to the result
            if current_sum == target:
                result.append(current_combination.copy())
                return

            # If the current sum exceeds the target or we've exhausted the candidates, stop exploring
            if current_sum > target or index == len(candidates):
                return

            # Include the current candidate and move to the next
            current_combination.append(candidates[index])
            dfs(index + 1, current_combination, current_sum + candidates[index])
            # Backtrack: remove the last added candidate
            current_combination.pop()

            # Skip over duplicate candidates to avoid repeating the same combination
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            # Exclude the current candidate and move to the next distinct candidate
            dfs(index + 1, current_combination, current_sum)

        # Start the DFS with an empty combination and a sum of 0
        dfs(0, [], 0)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2(candidates = [9,2,2,4,6,1,5], target = 8))
