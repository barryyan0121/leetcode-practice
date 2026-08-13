"""3850. 统计结果等于 K 的序列数目"""

from functools import lru_cache


class Solution:
    def countSequences(self, nums: list[int], k: int) -> int:
        def factors(value: int) -> tuple[int, int, int]:
            counts = []
            for prime in (2, 3, 5):
                count = 0
                while value % prime == 0:
                    value //= prime
                    count += 1
                counts.append(count)
            return (*counts, value)

        target2, target3, target5, rest = factors(k)
        if rest != 1:
            return 0
        deltas = []
        for value in nums:
            count2, count3, count5, _ = factors(value)
            deltas.append((count2, count3, count5))

        @lru_cache(maxsize=None)
        def dfs(index: int, exp2: int, exp3: int, exp5: int) -> int:
            if index == len(nums):
                return int((exp2, exp3, exp5) == (target2, target3, target5))
            d2, d3, d5 = deltas[index]
            return (
                dfs(index + 1, exp2, exp3, exp5)
                + dfs(index + 1, exp2 + d2, exp3 + d3, exp5 + d5)
                + dfs(index + 1, exp2 - d2, exp3 - d3, exp5 - d5)
            )

        return dfs(0, 0, 0, 0)


if __name__ == "__main__":
    test_cases = [(([2, 3, 2], 6), 2), (([4, 6, 3], 2), 2), (([1, 5], 1), 3)]
    for args, expected in test_cases:
        assert Solution().countSequences(*args) == expected
