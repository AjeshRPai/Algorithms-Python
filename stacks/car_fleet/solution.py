from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine each car's position and speed into a list of pairs
        cars = [(pos, spd) for pos, spd in zip(position, speed)]

        # Sort the cars by their position in descending order, so we process the car closest to the target first
        cars.sort(reverse=True)

        # Stack to track the time taken for each car (or fleet) to reach the target
        time_stack = []

        # Iterate through the cars in the sorted order
        for pos, spd in cars:
            # Calculate the time it takes for the car to reach the target
            time_stack.append((target - pos) / spd)
            # If there are at least two cars in the stack and the current car takes less or equal time
            # than the car in front, they form a fleet, so we don't need to track the current car separately
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                time_stack.pop()
            # Current car will merge with the previous fleet
            # so pop it

        # The number of fleets is the size of the stack
        return len(time_stack)


from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine each car's position and speed into a list of pairs
        cars = [(pos, spd) for pos, spd in zip(position, speed)]

        # Sort the cars by their position in descending order, so we process the car closest to the target first
        cars.sort(reverse=True)

        # Stack to track the time taken for each car (or fleet) to reach the target
        time_stack = []

        # Iterate through the cars in the sorted order
        for pos, spd in cars:
            # Calculate the time it takes for the car to reach the target
            time_to_reach_target = (target - pos) / spd
            # If there are at least two cars in the stack and the current car takes less or equal time
            # than the car in front, they form a fleet, so we don't need to track the current car separately
            if time_stack and time_to_reach_target <= time_stack[-1]:
                continue  # Current car will merge with the previous fleet
            # If the car doesn't merge, push its time to the stack (as a new fleet)
            time_stack.append(time_to_reach_target)

        # The number of fleets is the size of the stack
        return len(time_stack)

if __name__ == "__main__":
    solution = Solution()

    # Scenario 1: Example from problem description
    target1 = 12
    position1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]
    result1 = solution.carFleet(target1, position1, speed1)
    print(f"Scenario 1 - Fleets: {result1}")

    # Scenario 2: All cars have the same speed
    target2 = 100
    position2 = [10, 30, 50, 70]
    speed2 = [10, 10, 10, 10]
    result2 = solution.carFleet(target2, position2, speed2)
    print(f"Scenario 2 - Fleets: {result2}")

    # Scenario 3: Cars at the same position
    target3 = 50
    position3 = [25, 25, 25]
    speed3 = [1, 2, 3]
    result3 = solution.carFleet(target3, position3, speed3)
    print(f"Scenario 3 - Fleets: {result3}")

    # Scenario 4: One car is far ahead of the others
    target4 = 100
    position4 = [90, 50, 30]
    speed4 = [10, 5, 2]
    result4 = solution.carFleet(target4, position4, speed4)
    print(f"Scenario 4 - Fleets: {result4}")