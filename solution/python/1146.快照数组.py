from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self.history = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1] = (self.snap_id, val)
        else:
            self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        current = self.snap_id
        self.snap_id += 1
        return current

    def get(self, index: int, snap_id: int) -> int:
        position = bisect_right(self.history[index], (snap_id, float("inf"))) - 1
        return self.history[index][position][1]


if __name__ == "__main__":
    array = SnapshotArray(3)
    test_cases = [
        (array.set, (0, 5), None),
        (array.snap, (), 0),
        (array.get, (0, 0), 5),
        (array.set, (1, 7), None),
        (array.set, (1, 9), None),
        (array.snap, (), 1),
        (array.get, (1, 1), 9),
        (array.get, (2, 1), 0),
    ]
    for _, (method, args, expected) in enumerate(test_cases):
        assert method(*args) == expected
