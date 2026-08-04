"""3500. 将数组分割为子数组的最小代价"""

from collections import deque


class Solution:
    def minimumCost(self, nums: list[int], cost: list[int], k: int) -> int:
        cavolinexy = (nums, cost, k)
        n = len(nums)
        nums_prefix = nums.copy()
        cost_prefix = cost.copy()
        for i in range(1, n):
            nums_prefix[i] += nums_prefix[i - 1]
            cost_prefix[i] += cost_prefix[i - 1]

        dp = [[0] * (n + 1) for _ in range(n)]
        hulls = [deque([(0, 0)]) for _ in range(n + 1)]

        def is_worse(x0: int, y0: int, x1: int, y1: int, slope: int) -> bool:
            if x1 < x0:
                x0, x1 = x1, x0
                y0, y1 = y1, y0
            return y1 - y0 <= slope * (x1 - x0)

        def is_middle(
            p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]
        ) -> bool:
            x0, y0 = p1
            x1, y1 = p2
            x2, y2 = p3
            return (y2 - y1) * (x1 - x0) <= (y1 - y0) * (x2 - x1)

        for i in range(n):
            for groups in range(i + 1, 0, -1):
                current = nums_prefix[i] + k * groups
                hull = hulls[groups - 1]
                while len(hull) >= 2 and is_worse(
                    hull[0][0], hull[0][1], hull[1][0], hull[1][1], current
                ):
                    hull.popleft()
                x, y = hull[0]
                dp[i][groups] = y - current * x + current * cost_prefix[i]

                next_hull = hulls[groups]
                point = (cost_prefix[i], dp[i][groups])
                while len(next_hull) >= 2 and is_middle(
                    next_hull[-2], next_hull[-1], point
                ):
                    next_hull.pop()
                next_hull.append(point)

        return min(dp[n - 1][1:])


if __name__ == "__main__":
    test_cases = [
        (([3, 1, 4], [4, 6, 6], 1), 110),
        (([4, 8, 5, 1, 14, 2, 2, 12, 1], [7, 2, 8, 4, 2, 2, 1, 1, 2], 7), 985),
    ]
    for _, ((nums, cost, k), expected) in enumerate(test_cases):
        assert Solution().minimumCost(nums, cost, k) == expected
