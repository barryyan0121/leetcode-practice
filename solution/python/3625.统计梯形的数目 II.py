"""3625. 统计梯形的数目 II"""

from collections import Counter, defaultdict
from math import gcd


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        velmoranic = points
        slopes = defaultdict(Counter)
        slope_degrees = defaultdict(Counter)
        line_counts = Counter()
        line_degrees = defaultdict(Counter)
        midpoints = defaultdict(Counter)

        for i, (x1, y1) in enumerate(velmoranic):
            for j in range(i + 1, len(velmoranic)):
                x2, y2 = velmoranic[j]
                dx, dy = x2 - x1, y2 - y1
                divisor = gcd(abs(dx), abs(dy))
                dx //= divisor
                dy //= divisor
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slope = (dy, dx)
                slopes[slope][0] += 1
                slope_degrees[slope][i] += 1
                slope_degrees[slope][j] += 1
                line = dy * x1 - dx * y1
                line_counts[(slope, line)] += 1
                line_degrees[(slope, line)][i] += 1
                line_degrees[(slope, line)][j] += 1
                midpoints[(x1 + x2, y1 + y2)][slope] += 1

        base_pairs = 0
        for slope, counts in slopes.items():
            segments = counts[0]
            base_pairs += segments * (segments - 1) // 2
            base_pairs -= sum(
                degree * (degree - 1) // 2 for degree in slope_degrees[slope].values()
            )
        for key, segments in line_counts.items():
            base_pairs -= segments * (segments - 1) // 2
            base_pairs += sum(
                degree * (degree - 1) // 2 for degree in line_degrees[key].values()
            )

        parallelograms = 0
        for counts in midpoints.values():
            segments = sum(counts.values())
            parallelograms += segments * (segments - 1) // 2
            parallelograms -= sum(count * (count - 1) // 2 for count in counts.values())
        return base_pairs - parallelograms


if __name__ == "__main__":
    assert Solution().countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]) == 2
    assert Solution().countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]) == 1
    assert Solution().countTrapezoids([[82, 7], [82, -9], [82, -52], [82, 78]]) == 0
