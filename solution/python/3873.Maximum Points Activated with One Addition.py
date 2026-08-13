class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.component_size = [1] * size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            root_x, root_y = root_y, root_x
        elif self.rank[root_x] == self.rank[root_y]:
            self.rank[root_y] += 1
        self.parent[root_x] = root_y
        self.component_size[root_y] += self.component_size[root_x]

    def size(self, x: int) -> int:
        return self.component_size[self.find(x)]


class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        union_find = UnionFind(len(points))
        seen = [{}, {}]
        for index, (x, y) in enumerate(points):
            if x in seen[0]:
                union_find.union(index, seen[0][x])
            else:
                seen[0][x] = index
            if y in seen[1]:
                union_find.union(index, seen[1][y])
            else:
                seen[1][y] = index

        largest = 0
        second = 0
        for index in range(len(points)):
            if union_find.find(index) != index:
                continue
            size = union_find.size(index)
            if size > largest:
                largest, second = size, largest
            elif size > second:
                second = size
        return largest + second + 1


if __name__ == "__main__":
    test_cases = [
        ([[1, 1], [1, 2], [2, 2]], 4),
        ([[2, 2], [1, 1], [3, 3]], 3),
    ]
    for _, (points, expected) in enumerate(test_cases):
        assert Solution().maxActivated(points) == expected
