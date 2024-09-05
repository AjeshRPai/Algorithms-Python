from collections import Counter, deque
import heapq
from typing import List


# Key Intuitive Steps and Points:
# Counting Task Frequencies:
#
# We use Counter to count the frequency of each task, which helps in understanding how many times each task needs to be executed.
# Using a Max-Heap:
#
# We use a max-heap to always select the task with the highest remaining count. In Python, since heapq is a min-heap by default, we use negative counts to simulate a max-heap.
# Cooling Mechanism with a Queue:
#
# A deque (double-ended queue) is used to keep track of tasks that are in their cooling period. Each task in the queue is stored with its remaining count and the time when it can be executed again.
# Time Management:
#
# We increment the time with each iteration. During each time unit:
# We check if a task can be executed from the heap.
# If so, we decrease its count and add it to the cooling queue if it needs to be executed again.
# We also check if the front task in the cooling queue is ready to be moved back to the heap based on the current time.
# Returning the Total Time:
#
# The loop continues until both the heap and the cooling queue are empty, and we return the total time taken.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        task_counts = Counter(tasks)  # A dictionary where keys are tasks and values are their counts
        # Step 2: Create a max-heap based on task counts (using negative counts to simulate max-heap in Python)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)  # Convert list into a heap structure

        time = 0  # Variable to keep track of the total time units
        cool_down_queue = deque()  # Queue to manage cooling period of tasks

        # Step 3: Process the tasks
        while max_heap or cool_down_queue:
            time += 1  # Increment the time for each unit of work (or idle time)

            # If there are tasks available to execute
            if max_heap:
                # Pop the task with the highest frequency (most needed to be executed)
                current_task_count = 1 + heapq.heappop(max_heap)  # Increment because we're using negative values
                # If there are more instances of this task left, put it in the cooling queue
                if current_task_count:
                    # Add the task back into the queue with the time when it can be executed again
                    cool_down_queue.append((current_task_count, time + n))

            # Step 4: Check if any task in the cooling queue can be moved back to the heap
            if cool_down_queue and cool_down_queue[0][1] == time:
                # If the task has cooled down, push it back into the heap
                heapq.heappush(max_heap, cool_down_queue.popleft()[0])

        # Step 5: Return the total time taken to execute all tasks with cooling periods
        return time

# A A A B C
# A B C Idle A Idle Idle Idle A
