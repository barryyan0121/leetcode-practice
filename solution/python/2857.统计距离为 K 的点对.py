"""2857. 统计距离为 K 的点对"""

from collections import defaultdict


class Solution:
    def countPairs(self, coordinates: list[list[int]], k: int) -> int:
        counts = defaultdict(int)
        answer = 0
        for x, y in coordinates:
            for dx in range(k + 1):
                answer += counts[(x ^ dx, y ^ (k - dx))]
            counts[(x, y)] += 1
        return answer


if __name__ == "__main__":
    assert Solution().countPairs([[1, 1], [2, 2]], 6) == 1
