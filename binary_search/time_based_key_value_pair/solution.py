class TimeMap:
    def __init__(self):
        self.time_series = {}  # key: list of (timestamp, value) tuples

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_series:
            self.time_series[key] = []
        self.time_series[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_series:
            return ""

        values = self.time_series[key]
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                if mid == len(values) - 1 or values[mid + 1][0] > timestamp:
                    return values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ""


if __name__ == '__main__':
    time_map = TimeMap()

    # Test case 1: Basic functionality
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"

    # Test case 2: Multiple values for the same key
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"
    assert time_map.get("foo", 3) == "bar"

    # Test case 3: Non-existent key
    assert time_map.get("nonexistent", 1) == ""

    # Test case 4: Timestamp before any set operation
    assert time_map.get("foo", 0) == ""

    # Test case 5: Multiple keys
    time_map.set("key2", "value1", 5)
    time_map.set("key2", "value2", 10)
    time_map.set("key2", "value3", 15)
    assert time_map.get("key2", 7) == "value1"
    assert time_map.get("key2", 12) == "value2"
    assert time_map.get("key2", 20) == "value3"

    print("All tests passed!")

