from typing import List


class Solution:
    def bestTower(
        self, towers: List[List[int]], center: List[int], radius: int
    ) -> List[int]:
        best = None
        for x, y, quality in towers:
            if abs(x - center[0]) + abs(y - center[1]) <= radius:
                candidate = (quality, -x, -y)
                if best is None or candidate > best[0]:
                    best = (candidate, [x, y])
        return best[1] if best else [-1, -1]


if __name__ == "__main__":
    s = Solution()
    assert s.bestTower([[1, 2, 5], [2, 1, 7], [3, 1, 9]], [1, 1], 2) == [3, 1]
    assert s.bestTower([[1, 3, 4], [2, 2, 4], [4, 4, 7]], [0, 0], 5) == [1, 3]
    assert s.bestTower([[5, 6, 8], [0, 3, 5]], [1, 2], 1) == [-1, -1]
