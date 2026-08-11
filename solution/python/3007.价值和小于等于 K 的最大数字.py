"""3007. 价值和小于等于 K 的最大数字"""


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def price(num: int) -> int:
            total = 0
            bit = x - 1
            while (1 << bit) <= num:
                cycle = 1 << (bit + 1)
                full, rest = divmod(num + 1, cycle)
                total += full * (1 << bit) + max(0, rest - (1 << bit))
                bit += x
            return total

        left, right = 0, 10**16
        while left < right:
            middle = (left + right + 1) // 2
            if price(middle) <= k:
                left = middle
            else:
                right = middle - 1
        return left


if __name__ == "__main__":
    assert Solution().findMaximumNumber(9, 1) == 6
    assert Solution().findMaximumNumber(7, 2) == 9
    assert Solution().findMaximumNumber(1, 5) == 16
