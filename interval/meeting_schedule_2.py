from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Create a list to track the start and end times of meetings
        events = []

        # Add all start and end times as separate events
        for interval in intervals:
            events.append((interval.start, 1))  # 1 indicates a meeting starting
            events.append((interval.end, -1))  # -1 indicates a meeting ending

        # Sort events by time; if times are the same, sort by the type of event (-1 before 1)
        events.sort(key=lambda x: (x[0], x[1]))

        # Initialize counters
        current_rooms = 0  # Tracks the current number of active meeting rooms
        max_rooms = 0  # Tracks the maximum number of rooms required at any time

        # Iterate through all events
        for event in events:
            # Adjust the count of current rooms based on whether a meeting starts or ends
            current_rooms += event[1]
            # Update the maximum number of rooms required
            max_rooms = max(max_rooms, current_rooms)

        # Return the maximum number of rooms required
        return max_rooms