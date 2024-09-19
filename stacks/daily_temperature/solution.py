from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result list with all 0s, which will hold the number of days to wait for a warmer temperature
        result = [0] * len(temperatures)

        # Stack to keep track of temperatures and their indices (as pairs)
        stack = []  # Format: [(temperature, index)]

        # Loop through the list of temperatures
        for currentIndex, currentTemp in enumerate(temperatures):
            # While the current temperature is warmer than the temperature at the top of the stack
            while stack and currentTemp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()  # Get the temperature and its index from the stack
                result[stackIndex] = currentIndex - stackIndex  # Calculate the number of days
            # Push the current temperature and its index onto the stack
            stack.append((currentTemp, currentIndex))

        # Return the result list, which contains the number of days for each temperature
        return result


if __name__ == "__main__":
    solution = Solution()

    # Scenario 1: Simple example
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    result1 = solution.dailyTemperatures(temperatures1)
    print(f"Scenario 1 - Input: {temperatures1}, Output: {result1}")

    # Scenario 2: All temperatures increasing
    temperatures2 = [60, 62, 64, 66, 68]
    result2 = solution.dailyTemperatures(temperatures2)
    print(f"Scenario 2 - Input: {temperatures2}, Output: {result2}")

    # Scenario 3: No warmer day in the future
    temperatures3 = [80, 79, 78, 77, 76]
    result3 = solution.dailyTemperatures(temperatures3)
    print(f"Scenario 3 - Input: {temperatures3}, Output: {result3}")

    # Scenario 4: All temperatures the same
    temperatures4 = [70, 70, 70, 70]
    result4 = solution.dailyTemperatures(temperatures4)
    print(f"Scenario 4 - Input: {temperatures4}, Output: {result4}")

    temperature5 = [30,38,30,36,35,40,28]
    result5 = solution.dailyTemperatures(temperature5)
    print(f"Scenario 5 - Input: {temperature5}, Output: {result5}")