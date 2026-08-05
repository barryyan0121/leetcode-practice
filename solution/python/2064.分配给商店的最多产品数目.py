"""2064. 分配给商店的最多产品数目"""


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        low, high = 1, max(quantities)
        while low < high:
            middle = (low + high) // 2
            if sum((value + middle - 1) // middle for value in quantities) <= n:
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [((6, [11, 6]), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimizedMaximum(*args) == expected
