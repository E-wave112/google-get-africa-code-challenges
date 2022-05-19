class MyHashMap:
    def __init__(self):
        self.container = dict()

    def put(self, key: int, value: int) -> None:
        self.container[key] = value

    def get(self, key: int) -> int:
        if key not in self.container:
            return -1
        return self.container.get(key)

    def remove(self, key: int):
        if key not in self.container:
            return -1
        self.container.pop(key)
