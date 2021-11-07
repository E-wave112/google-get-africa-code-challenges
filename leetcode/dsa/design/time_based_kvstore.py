class TimeMap:

    def __init__(self):
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key] = [value, timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if self.time[key] or self.time[key][-1] != timestamp:
            return self.time[key][0]
        return self.time.get(key[0], "")
