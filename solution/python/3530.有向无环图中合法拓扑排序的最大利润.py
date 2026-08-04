"""3530. 有向无环图中合法拓扑排序的最大利润"""

from functools import cache


class Solution:
    def maxProfit(self, n: int, edges: list[list[int]], score: list[int]) -> int:
        prerequisites = [0] * n
        for source, target in edges:
            prerequisites[target] |= 1 << source

        full = (1 << n) - 1

        @cache
        def best(mask: int) -> int:
            if mask == full:
                return 0
            position = mask.bit_count() + 1
            answer = 0
            for node in range(n):
                if (
                    mask >> node & 1 == 0
                    and mask & prerequisites[node] == prerequisites[node]
                ):
                    answer = max(
                        answer, best(mask | 1 << node) + position * score[node]
                    )
            return answer

        return best(0)


if __name__ == "__main__":
    test_cases = [
        ((2, [], [1, 2]), 5),
        ((3, [[0, 1], [1, 2]], [1, 2, 3]), 14),
        ((3, [[0, 2]], [5, 1, 10]), 41),
    ]
    for _, ((n, edges, score), expected) in enumerate(test_cases):
        assert Solution().maxProfit(n, edges, score) == expected
