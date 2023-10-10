class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def binary_search(self, timestamps, target):
        left, right = 0, len(timestamps) - 1
        while left <= right:
            mid = (left + right) // 2
            if timestamps[mid][0] == target:
                return mid
            elif timestamps[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            timestamps = self.time_map[key]
            index = self.binary_search(timestamps, timestamp)
            if index >= 0:
                return timestamps[index][1]
        return ""