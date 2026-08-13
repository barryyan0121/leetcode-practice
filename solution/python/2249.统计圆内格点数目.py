"""2249. 统计圆内格点数目"""


class Solution:
    def countLatticePoints(self, circles: list[list[int]]) -> int:
        points = set()
        for x, y, radius in circles:
            for i in range(x - radius, x + radius + 1):
                for j in range(y - radius, y + radius + 1):
                    if (i - x) ** 2 + (j - y) ** 2 <= radius * radius:
                        points.add((i, j))
        return len(points)

if __name__ == "__main__":
    assert Solution().countLatticePoints([[2,2,1]]) == 5
