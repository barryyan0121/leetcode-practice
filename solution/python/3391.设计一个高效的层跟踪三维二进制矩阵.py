"""3391. 设计一个高效的层跟踪三维二进制矩阵"""


class Matrix3D:
    def __init__(self, n: int):
        self.cells = [set() for _ in range(n)]
        self.counts = [0] * n

    def setCell(self, x: int, y: int, z: int) -> None:
        if (y, z) not in self.cells[x]:
            self.cells[x].add((y, z))
            self.counts[x] += 1

    def unsetCell(self, x: int, y: int, z: int) -> None:
        if (y, z) in self.cells[x]:
            self.cells[x].remove((y, z))
            self.counts[x] -= 1

    def largestMatrix(self) -> int:
        maximum = max(self.counts)
        return max(index for index, count in enumerate(self.counts) if count == maximum)


if __name__ == "__main__":
    test_cases = [((3,), [None])]
    for _, (args, expected) in enumerate(test_cases):
        assert args == (3,) and expected == [None]
    matrix = Matrix3D(3)
    matrix.setCell(0, 0, 0)
    assert matrix.largestMatrix() == 0
    matrix.setCell(1, 1, 2)
    assert matrix.largestMatrix() == 1
    matrix.setCell(0, 0, 1)
    assert matrix.largestMatrix() == 0
