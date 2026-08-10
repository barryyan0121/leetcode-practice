class MRUQueue:
    def __init__(self, n: int):
        self.queue = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        value = self.queue.pop(k - 1)
        self.queue.append(value)
        return value


if __name__ == "__main__":
    queue = MRUQueue(8)
    assert queue.fetch(3) == 3
    assert queue.fetch(5) == 6
    assert queue.fetch(2) == 2
    print("1756 passed")
