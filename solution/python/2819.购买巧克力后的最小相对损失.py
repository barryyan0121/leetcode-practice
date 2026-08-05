from itertools import accumulate


class Solution:
    def minimumRelativeLosses(
        self, prices: list[int], queries: list[list[int]]
    ) -> list[int]:
        prices.sort()
        prefix = [0] + list(accumulate(prices))
        n = len(prices)

        def loss(k: int, m: int, left: int) -> int:
            right = m - left
            suffix_start = n - right
            return prefix[left] + 2 * k * right - (prefix[n] - prefix[suffix_start])

        ans = []
        for k, m in queries:
            lo, hi = 0, m
            while hi - lo > 2:
                a = lo + (hi - lo) // 3
                b = hi - (hi - lo) // 3
                if loss(k, m, a) <= loss(k, m, b):
                    hi = b
                else:
                    lo = a
            ans.append(min(loss(k, m, left) for left in range(lo, hi + 1)))
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumRelativeLosses([1, 9, 22, 10, 19], [[18, 4], [5, 2]]) == [
        34,
        -21,
    ]
    assert solution.minimumRelativeLosses([5, 6, 7], [[10, 1], [5, 3], [3, 3]]) == [
        5,
        12,
        0,
    ]
