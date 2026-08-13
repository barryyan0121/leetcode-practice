"""3235. 判断矩形的两个角落是否可达"""


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return
        if self.rank[root_left] < self.rank[root_right]:
            self.parent[root_left] = root_right
        elif self.rank[root_left] > self.rank[root_right]:
            self.parent[root_right] = root_left
        else:
            self.parent[root_left] = root_right
            self.rank[root_right] += 1


class Solution:
    def canReachCorner(
        self, xCorner: int, yCorner: int, circles: list[list[int]]
    ) -> bool:
        n = len(circles)
        uf = UnionFind(n + 2)
        start = n
        end = n + 1

        for index, (x, y, radius) in enumerate(circles):
            if x - radius <= 0 or y + radius >= yCorner:
                uf.union(index, start)
            if x + radius >= xCorner or y - radius <= 0:
                uf.union(index, end)
            for other in range(index):
                x2, y2, radius2 = circles[other]
                if (x - x2) ** 2 + (y - y2) ** 2 <= (radius + radius2) ** 2:
                    uf.union(index, other)

        return uf.find(start) != uf.find(end)


if __name__ == "__main__":
    test_cases = [
        ((3, 4, [[2, 1, 1]]), True),
        ((3, 3, [[1, 1, 2]]), False),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().canReachCorner(*args) == expected
